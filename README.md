#Django active navigation

Provides some simple template tags for highlighting active navigation links in Django templates.

## Installation

The application is available using pip/easy_install:

    pip install django-active-navigation
    easy_install django-active-navigation
    
You will also need to install django-classy-tags:

    pip install django-classy-tags
    easy_install django-classy-tags
    
Then just add 'active_navigation' to your INSTALLED_APPS setting and you're away!

## Usage

Four template tags are provided depending on whether you want exact matches or not and whether you're using named URLs. They all have the same format and possibilities:

    {% tag_name request url %}
    {% tag_name request url active_class %}
    {% tag_name request url active_class as variable_name %}

* request is the HttpRequest object obtained from using RequestContext.
* By default the tag will return 'active' for an active url, and '' if it isn't active. Define active_class to have it return something different.
* To have the template tag return the result into a variable define variable_name

### active_exact

Match the current url exactly to the given url. If the current URL is /modules:

    {% active_exact request /modules %} returns 'active'
    {% active_exact request /modules/module %} returns ''
    {% active_exact request /modules 'myclass' %} returns 'myclass'
    {% active_exact request /modules 'myclass' as is_active %} returns '', but the variable is_active contains 'myclass'
