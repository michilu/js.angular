import os.path
from fanstatic import Library, Resource

library = Library('angularjs', 'resources')

angular                       = Resource(library, 'angular.js',
                                         minified='angular.min.js')
angular_animate               = Resource(library, 'angular-animate.js',
                                         minified='angular-animate.min.js',
                                         depends=[angular])
angular_bootstrap             = Resource(library, 'angular-bootstrap.js',
                                         minified='angular-bootstrap.min.js',
                                         depends=[angular])
angular_bootstrap_prettify    = Resource(library, 'angular-bootstrap-prettify.js',
                                         minified='angular-bootstrap-prettify.min.js',
                                         depends=[angular])
angular_cookies               = Resource(library, 'angular-cookies.js',
                                         minified='angular-cookies.min.js',
                                         depends=[angular])
angular_loader                = Resource(library, 'angular-loader.js',
                                         minified='angular-loader.min.js')
angular_mobile                = Resource(library, 'angular-mobile.js',
                                         minified='angular-mobile.min.js',
                                         depends=[angular])
angular_mocks                 = Resource(library, 'angular-mocks.js',
                                         depends=[angular])
angular_resource              = Resource(library, 'angular-resource.js',
                                         minified='angular-resource.min.js',
                                         depends=[angular])
angular_route                 = Resource(library, 'angular-route.js',
                                         minified='angular-route.min.js',
                                         depends=[angular])
angular_sanitize              = Resource(library, 'angular-sanitize.js',
                                         minified='angular-sanitize.min.js',
                                         depends=[angular])
angular_scenario              = Resource(library, 'angular-scenario.js')

angular_touch                 = Resource(library, 'angular-touch.js',
                                         minified='angular-touch.min.js',
                                         depends=[angular])

for filename in [f for f in os.listdir(os.path.join(library.path, 'i18n'))
        if os.path.splitext(f)[1] == '.js']:
    resource_name = filename.replace('-', '_')[:-3]
    locals()[resource_name] = Resource(library, 'i18n/{0}'.format(filename))
