"""
Testing for the active navigation template tags
"""

from django.core.urlresolvers import reverse
from django.template import Context, RequestContext, Template
from django.test import  TestCase
from django.test.client import RequestFactory

class ActiveNavigationTagsTestCase(TestCase):

    urls = 'active_navigation.test_urls'

    def setUp(self):
        self.factory = RequestFactory()

class ActiveNavigationTagsTests(ActiveNavigationTagsTestCase):

    def test_can_load_tags(self):

        request = self.factory.get('/')
        context = RequestContext(request, {
            'request': request
        })

        # Any undefined tag will throw an exception that will cause the test to fail!
        output = Template(
            "{% load active_navigation_tags %}"
            "{% active request '/' %}"
            "{% active_exact request '/' %}"
            "{% reverse_active request 'index' %}"
            "{% reverse_active_exact request 'index' %}"
        ).render(context)

class ActiveExactTests(ActiveNavigationTagsTestCase):

    def test_active_exact_is_active(self):

        request = self.factory.get('/')
        context = RequestContext(request, {
            'request': request
        })

        output = Template(
            "{% load active_navigation_tags %}"
            "{% active_exact request '/' %}"
        ).render(context)

        self.assertEqual(output, 'active')

    def test_active_exact_is_not_active(self):

        request = self.factory.get('/not-active')
        context = RequestContext(request, {
            'request': request
        })

        output = Template(
            "{% load active_navigation_tags %}"
            "{% active_exact request '/' %}"
        ).render(context)

        self.assertEqual(output, '')

    def test_active_exact_is_active_active_class(self):

        request = self.factory.get('/')
        context = RequestContext(request, {
            'request': request
        })

        output = Template(
            "{% load active_navigation_tags %}"
            "{% active_exact request '/' 'myclass' %}"
        ).render(context)

        self.assertEqual(output, 'myclass')

    # If the url isn't active then we expect the template not to contain the active class
    # Tests this with a custom active class
    def test_active_exact_is_not_active_active_class(self):

        request = self.factory.get('/')
        context = RequestContext(request, {
            'request': request
        })

        output = Template(
            "{% load active_navigation_tags %}"
            "{% active_exact request '/not-active' 'myclass' %}"
        ).render(context)

        self.assertEqual(output, '')

    def test_active_exact_is_active_return(self):

        request = self.factory.get('/')
        context = RequestContext(request, {
            'request': request
        })

        output = Template(
            "{% load active_navigation_tags %}"
            "{% active_exact request '/' 'active' as is_active %}"
        ).render(context)

        self.assertEqual(output, '')
        self.assertIn('is_active', context)
        self.assertEqual(context['is_active'], 'active')

    def test_active_exact_is_not_active_return(self):

        request = self.factory.get('/')
        context = RequestContext(request, {
            'request': request
        })

        output = Template(
            "{% load active_navigation_tags %}"
            "{% active_exact request '/not-active' 'active' as is_active %}"
        ).render(context)

        # The tag should not render anything
        self.assertEqual(output, '')

        # The variable is_active should be in the context
        self.assertIn('is_active', context)

        # And the new context variable should be empty
        self.assertEqual(context['is_active'], '')

    def test_active_exact_is_active_active_class_return(self):

        request = self.factory.get('/')
        context = RequestContext(request, {
            'request': request
        })

        output = Template(
            "{% load active_navigation_tags %}"
            "{% active_exact request '/' 'myclass' as is_active %}"
        ).render(context)

        self.assertEqual(output, '')
        self.assertIn('is_active', context)
        self.assertEqual(context['is_active'], 'myclass')

    def test_active_exact_is_not_active_active_class_return(self):

        request = self.factory.get('/')
        context = RequestContext(request, {
            'request': request
        })

        output = Template(
            "{% load active_navigation_tags %}"
            "{% active_exact request '/not-active' 'myclass' as is_active %}"
        ).render(context)

        self.assertEqual(output, '')
        self.assertIn('is_active', context)
        self.assertEqual(context['is_active'], '')

class ActiveTests(ActiveNavigationTagsTestCase):

    def test_active_is_active_exact(self):

        request = self.factory.get('/')
        context = RequestContext(request, {
            'request': request
        })

        output = Template(
            "{% load active_navigation_tags %}"
            "{% active request '/' %}"
        ).render(context)

        self.assertEqual(output, 'active')

    def test_active_is_active_startswith(self):

        request = self.factory.get('/modules/test_module/sublink')
        context = RequestContext(request, {
            'request': request
        })

        output = Template(
            "{% load active_navigation_tags %}"
            "{% active request '/modules/' %}"
        ).render(context)

        self.assertEqual(output, 'active')

    def test_active_is_not_active(self):

        request = self.factory.get('/modules')
        context = RequestContext(request, {
            'request': request
        })

        output = Template(
            "{% load active_navigation_tags %}"
            "{% active request '/blog' %}"
        ).render(context)

        self.assertEqual(output, '')

    def test_active_is_active_active_class(self):

        request = self.factory.get('/modules/module')
        context = RequestContext(request, {
            'request': request
        })

        output = Template(
            "{% load active_navigation_tags %}"
            "{% active request '/modules' 'myclass' %}"
        ).render(context)

        self.assertEqual(output, 'myclass')

    def test_active_is_not_active_active_class(self):

        request = self.factory.get('/blog')
        context = RequestContext(request, {
            'request': request
        })

        output = Template(
            "{% load active_navigation_tags %}"
            "{% active request '/modules' 'myclass' %}"
        ).render(context)

        self.assertEqual(output, '')

    def test_active_is_active_active_class_return(self):

        request = self.factory.get('/modules/module')
        context = RequestContext(request, {
            'request': request
        })

        output = Template(
            "{% load active_navigation_tags %}"
            "{% active request '/modules' 'myclass' as is_active %}"
        ).render(context)

        self.assertIn('is_active', context)
        self.assertEqual(context['is_active'], 'myclass')

    def test_active_is_not_active_active_class_return(self):

        request = self.factory.get('/blog')
        context = RequestContext(request, {
            'request': request
        })

        output = Template(
            "{% load active_navigation_tags %}"
            "{% active request '/modules' 'myclass' as is_active %}"
        ).render(context)

        self.assertIn('is_active', context)
        self.assertEqual(context['is_active'], '')

class ReverseActiveExactTests(ActiveNavigationTagsTestCase):

    def test_reverse_active_exact_is_active_exact(self):

        request = self.factory.get(reverse('modules'))
        context = RequestContext(request, {
            'request': request
        })

        output = Template(
            "{% load active_navigation_tags %}"
            "{% reverse_active_exact request 'modules' %}"
        ).render(context)

        self.assertEqual(output, 'active')

    def test_reverse_active_exact_is_not_active_exact(self):

        request = self.factory.get(reverse('index'))
        context = RequestContext(request, {
            'request': request
        })

        output = Template(
            "{% load active_navigation_tags %}"
            "{% reverse_active_exact request 'modules' %}"
        ).render(context)

        self.assertEqual(output, '')

    def test_reverse_active_exact_is_active_active_class(self):

        request = self.factory.get(reverse('modules'))
        context = RequestContext(request, {
            'request': request
        })

        output = Template(
            "{% load active_navigation_tags %}"
            "{% reverse_active_exact request 'modules' 'myclass' %}"
        ).render(context)

        self.assertEqual(output, 'myclass')

    def test_reverse_active_exact_is_not_active_active_class(self):

        request = self.factory.get(reverse('index'))
        context = RequestContext(request, {
            'request': request
        })

        output = Template(
            "{% load active_navigation_tags %}"
            "{% reverse_active_exact request 'modules' 'myclass' %}"
        ).render(context)

        self.assertEqual(output, '')

    def test_reverse_active_exact_is_active_active_class_return(self):

        request = self.factory.get(reverse('modules'))
        context = RequestContext(request, {
            'request': request
        })

        output = Template(
            "{% load active_navigation_tags %}"
            "{% reverse_active_exact request 'modules' 'myclass' as is_active %}"
        ).render(context)

        self.assertEqual(output, '')
        self.assertIn('is_active', context)
        self.assertEqual(context['is_active'], 'myclass')

    def test_reverse_active_exact_is_not_active_active_class_return(self):

        request = self.factory.get(reverse('index'))
        context = RequestContext(request, {
            'request': request
        })

        output = Template(
            "{% load active_navigation_tags %}"
            "{% reverse_active_exact request 'modules' 'myclass' as is_active %}"
        ).render(context)

        self.assertEqual(output, '')
        self.assertIn('is_active', context)
        self.assertEqual(context['is_active'], '')

class ReverseActiveTests(ActiveNavigationTagsTestCase):

    def test_reverse_active_is_active_exact(self):

        request = self.factory.get(reverse('modules'))
        context = RequestContext(request, {
            'request': request
        })

        output = Template(
            "{% load active_navigation_tags %}"
            "{% reverse_active request 'modules' %}"
        ).render(context)

        self.assertEqual(output, 'active')

    def test_reverse_active_is_not_active_exact(self):

        request = self.factory.get(reverse('index'))
        context = RequestContext(request, {
            'request': request
        })

        output = Template(
            "{% load active_navigation_tags %}"
            "{% reverse_active request 'modules' %}"
        ).render(context)

        self.assertEqual(output, '')

    def test_reverse_active_is_active_startswith(self):

        request = self.factory.get(reverse('module'))
        context = RequestContext(request, {
            'request': request
        })

        output = Template(
            "{% load active_navigation_tags %}"
            "{% reverse_active request 'modules' %}"
        ).render(context)

        self.assertEqual(output, 'active')

    def test_reverse_active_is_not_active_startswith(self):

        request = self.factory.get(reverse('blog'))
        context = RequestContext(request, {
            'request': request
        })

        output = Template(
            "{% load active_navigation_tags %}"
            "{% reverse_active request 'modules' %}"
        ).render(context)

        self.assertEqual(output, '')

    def test_reverse_active_is_active_active_class(self):

        request = self.factory.get(reverse('modules'))
        context = RequestContext(request, {
            'request': request
        })

        output = Template(
            "{% load active_navigation_tags %}"
            "{% reverse_active request 'modules' 'myclass' %}"
        ).render(context)

        self.assertEqual(output, 'myclass')

    def test_reverse_active_is_not_active_active_class(self):

        request = self.factory.get(reverse('index'))
        context = RequestContext(request, {
            'request': request
        })

        output = Template(
            "{% load active_navigation_tags %}"
            "{% reverse_active request 'modules' 'myclass' %}"
        ).render(context)

        self.assertEqual(output, '')

    def test_reverse_active_is_active_active_class_return(self):

        request = self.factory.get(reverse('modules'))
        context = RequestContext(request, {
            'request': request
        })

        output = Template(
            "{% load active_navigation_tags %}"
            "{% reverse_active request 'modules' 'myclass' as is_active %}"
        ).render(context)

        self.assertEqual(output, '')
        self.assertIn('is_active', context)
        self.assertEqual(context['is_active'], 'myclass')

    def test_reverse_active_is_not_active_active_class_return(self):

        request = self.factory.get(reverse('index'))
        context = RequestContext(request, {
            'request': request
        })

        output = Template(
            "{% load active_navigation_tags %}"
            "{% reverse_active request 'modules' 'myclass' as is_active %}"
        ).render(context)

        self.assertEqual(output, '')
        self.assertIn('is_active', context)
        self.assertEqual(context['is_active'], '')