output = ['\n'
          'Recent Questions - Stack Overflow\n',
          '\n'
          '---------------------------------------------------------------\n'
          'Please tell me how to run this java code with servlet in vscode\n'
          '---------------------------------------------------------------\n',
          'Author: SlumpShrimp',
          'Link: https://stackoverflow.com/questions/59273035/please-tell-me-how-to-run-this-java-code-with-servlet'
          '-in-vscode',
          'Published: Tuesday, 10 December 2019 18:03:53',
          "\n"
          "I wanna develop a dynamic web application using vscode. However, I can't solve\n"
          "this problem. So, please give me some advises.\n"
          "\n"
          "[Error message](https://i.stack.imgur.com/102ht.png)\n",
          'Links:',
          'https://stackoverflow.com/questions/59273035/please-tell-me-how-to-run-this-java-code-with-servlet-in'
          '-vscode',
          '\n'
          '------------------------------------------------------------\n'
          'hi, help in solving the problem, I don’t know where to start\n'
          '------------------------------------------------------------\n',
          'Author: An Mal',
          'Link: https://stackoverflow.com/questions/59273034/hi-help-in-solving-the-problem-i-don-t-know-where-to'
          '-start',
          'Published: Tuesday, 10 December 2019 18:03:52',
          '\n'
          'Given file f, whose components are character arrays s1, ..., s10. Get in the\n'
          'f1 file character arrays of twenty elements each. These arrays should be\n'
          'obtained by the following transformations of the original arrays: s10, ...,\n'
          's1, s1, ..., s10\n',
          'Links:',
          'https://stackoverflow.com/questions/59273034/hi-help-in-solving-the-problem-i-don-t-know-where-to-start']

printed_output = """
Recent Questions - Stack Overflow


---------------------------------------------------------------
Please tell me how to run this java code with servlet in vscode
---------------------------------------------------------------

Author: SlumpShrimp
Link: https://stackoverflow.com/questions/59273035/please-tell-me-how-to-run-this-java-code-with-servlet-in-vscode
Published: Tuesday, 10 December 2019 18:03:53

I wanna develop a dynamic web application using vscode. However, I can't solve
this problem. So, please give me some advises.

[Error message](https://i.stack.imgur.com/102ht.png)

Links:
https://stackoverflow.com/questions/59273035/please-tell-me-how-to-run-this-java-code-with-servlet-in-vscode

------------------------------------------------------------
hi, help in solving the problem, I don’t know where to start
------------------------------------------------------------

Author: An Mal
Link: https://stackoverflow.com/questions/59273034/hi-help-in-solving-the-problem-i-don-t-know-where-to-start
Published: Tuesday, 10 December 2019 18:03:52

Given file f, whose components are character arrays s1, ..., s10. Get in the
f1 file character arrays of twenty elements each. These arrays should be
obtained by the following transformations of the original arrays: s10, ...,
s1, s1, ..., s10

Links:
https://stackoverflow.com/questions/59273034/hi-help-in-solving-the-problem-i-don-t-know-where-to-start
"""

json = {
    "title": "Recent Questions - Stack Overflow",
    "entries": [
        {
            "title": "Please tell me how to run this java code with servlet in vscode",
            "author": "SlumpShrimp",
            "link": "https://stackoverflow.com/questions/59273035/please-tell-me-how-to-run-this-java-code-with"
                    "-servlet-in-vscode",
            "published": "2019-12-10T18:03:53Z",
            "summary": "<p>I wanna develop a dynamic web application using vscode. However, I can't solve this "
                       "problem.\nSo, please give me some advises.</p>\n\n<p><a "
                       "href=\"https://i.stack.imgur.com/102ht.png\" rel=\"nofollow noreferrer\">Error "
                       "message</a></p>",
            "links": [
                {
                    "rel": "alternate",
                    "href": "https://stackoverflow.com/questions/59273035/please-tell-me-how-to-run-this"
                            "-java-code-with-servlet-in-vscode",
                    "type": "text/html"
                }
            ]
        },
        {
            "title": "hi, help in solving the problem, I don\u2019t know where to start",
            "author": "An Mal",
            "link": "https://stackoverflow.com/questions/59273034/hi-help-in-solving-the-problem-i-don-t-know-where"
                    "-to-start",
            "published": "2019-12-10T18:03:52Z",
            "summary": "<p>Given file f, whose components are character arrays s1, ..., s10. Get in the f1 file "
                       "character arrays of twenty elements each. These arrays should be obtained by the following "
                       "transformations of the original arrays: s10, ..., s1, s1, ..., s10</p>",
            "links": [
                {
                    "rel": "alternate",
                    "href": "https://stackoverflow.com/questions/59273034/hi-help-in-solving-the-problem-i"
                            "-don-t-know-where-to-start",
                    "type": "text/html"
                }
            ]
        }
    ]
}

empty_feed = {"entries": []}

feed = {'bozo': False,
        'entries': [{'id': 'https://stackoverflow.com/q/59273035', 'guidislink': True,
                     'link': 'https://stackoverflow.com/questions/59273035/please-tell-me-how-to-run-this-java-code'
                             '-with-servlet-in-vscode',
                     're_rank': {'scheme': 'https://stackoverflow.com'},
                     'title': 'Please tell me how to run this java code with servlet in vscode',
                     'title_detail': {'type': 'text/plain', 'language': None,
                                      'base': 'https://stackoverflow.com/feeds/',
                                      'value': 'Please tell me how to run this java code with '
                                               'servlet in vscode'},
                     'tags': [{'term': 'java', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None},
                              {'term': 'servlets', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None}, {'term': 'visual-studio-code',
                                                'scheme': 'https://stackoverflow.com/tags',
                                                'label': None}],
                     'authors': [{'name': 'SlumpShrimp', 'href': 'https://stackoverflow.com/users/12502703'}],
                     'author_detail': {'name': 'SlumpShrimp', 'href': 'https://stackoverflow.com/users/12502703'},
                     'href': 'https://stackoverflow.com/users/12502703',
                     'author': 'SlumpShrimp',
                     'links': [{'rel': 'alternate', 'href': 'https://stackoverflow.com/questions/59273035/please-tell'
                                                            '-me-how-to-run-this-java-code-with-servlet-in-vscode',
                                'type': 'text/html'}],
                     'published': '2019-12-10T18:03:53Z',
                     'updated': '2019-12-10T18:03:53Z',
                     'summary': '<p>I wanna develop a dynamic web application using vscode. '
                                'However, I can\'t solve this problem.\nSo, please give me '
                                'some advises.</p>\n\n<p><a '
                                'href="https://i.stack.imgur.com/102ht.png" rel="nofollow '
                                'noreferrer">Error message</a></p>',
                     'summary_detail': {'type': 'text/html', 'language': None,
                                        'base': 'https://stackoverflow.com/feeds/',
                                        'value': '<p>I wanna develop a dynamic web application using vscode. However, '
                                                 'I can\'t solve this problem.\nSo, please give me some '
                                                 'advises.</p>\n\n<p><a href="https://i.stack.imgur.com/102ht.png" '
                                                 'rel="nofollow noreferrer">Error message</a></p>'}
                     },
                    {'id': 'https://stackoverflow.com/q/59273034', 'guidislink': True,
                     'link': 'https://stackoverflow.com/questions/59273034/hi-help-in-solving-the-problem-i-don-t'
                             '-know-where-to-start',
                     're_rank': {'scheme': 'https://stackoverflow.com'},
                     'title': 'hi, help in solving the problem, I don’t know where to start',
                     'title_detail': {'type': 'text/plain', 'language': None,
                                      'base': 'https://stackoverflow.com/feeds/',
                                      'value': 'hi, help in solving the problem, I don’t know where to start'},
                     'tags': [{'term': 'java', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None}],
                     'authors': [{'name': 'An Mal', 'href': 'https://stackoverflow.com/users/12513355'}],
                     'author_detail': {'name': 'An Mal', 'href': 'https://stackoverflow.com/users/12513355'},
                     'href': 'https://stackoverflow.com/users/12513355', 'author': 'An Mal',
                     'links': [{'rel': 'alternate',
                                'href': 'https://stackoverflow.com/questions/59273034/hi-help-in-solving-the'
                                        '-problem'
                                        '-i-don-t-know-where-to-start', 'type': 'text/html'}],
                     'published': '2019-12-10T18:03:52Z', 'updated': '2019-12-10T18:03:52Z',
                     'summary': '<p>Given file f, whose components are character arrays s1, '
                                '..., s10. Get in the f1 file character arrays of twenty '
                                'elements each. These arrays should be obtained by the '
                                'following transformations of the original arrays: s10, ..., '
                                's1, s1, ..., s10</p>',
                     'summary_detail': {'type': 'text/html', 'language': None,
                                        'base': 'https://stackoverflow.com/feeds/',
                                        'value': '<p>Given file f, whose components are '
                                                 'character arrays s1, ..., s10. Get in the '
                                                 'f1 file character arrays of twenty elements '
                                                 'each. These arrays should be obtained by '
                                                 'the following transformations of the '
                                                 'original arrays: s10, ..., s1, s1, ..., '
                                                 's10</p>'}},
                    {'id': 'https://stackoverflow.com/q/59273033', 'guidislink': True,
                     'link': 'https://stackoverflow.com/questions/59273033/amazon-cognito-how-change'
                             '-password-and-catch-console-exceptions',
                     're_rank': {'scheme': 'https://stackoverflow.com'},
                     'title': 'Amazon cognito how change password and catch console exceptions',
                     'title_detail': {'type': 'text/plain', 'language': None,
                                      'base': 'https://stackoverflow.com/feeds/',
                                      'value': 'Amazon cognito how change password and catch '
                                               'console exceptions'},
                     'tags': [{'term': 'ios', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None},
                              {'term': 'swift', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None},
                              {'term': 'amazon-s3', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None}], 'authors': [{'name': 'KarmelE98',
                                                             'href':
                                                                 'https://stackoverflow.com/users/11110173'}],
                     'author_detail': {'name': 'KarmelE98',
                                       'href': 'https://stackoverflow.com/users/11110173'},
                     'href': 'https://stackoverflow.com/users/11110173', 'author': 'KarmelE98',
                     'links': [{'rel': 'alternate',
                                'href':
                                    'https://stackoverflow.com/questions/59273033/amazon-cognito-how-change-password'
                                    '-and-catch-console-exceptions',
                                'type': 'text/html'}], 'published': '2019-12-10T18:03:49Z',
                     'updated': '2019-12-10T18:03:49Z',
                     'summary': '<p>My function which change password:</p>\n\n<pre><code>func '
                                'changePassword(oldPassword: String, newPassword: String){'
                                '\n\n        AppDelegate.defaultUserPool().currentUser('
                                ')?.changePassword(oldPassword, proposedPassword: '
                                'newPassword)\n\n\n        AppDelegate.defaultUserPool('
                                ').currentUser()?.clearSession()\n\n\n    '
                                '}\n</code></pre>\n\n<p>It works quite well, but I don\'t '
                                'know how to catch console exceptions (for example when I '
                                'write bad old password)</p>\n\n<pre><code>Response body:\n{'
                                '"__type":"NotAuthorizedException","message":"Incorrect '
                                'username or password."}\n\n"x-amzn-errormessage" = '
                                '"Incorrect username or password.";\n    "x-amzn-errortype" = '
                                '"NotAuthorizedException:";\n</code></pre>\n\n<p>How handle '
                                'it all?</p>',
                     'summary_detail': {'type': 'text/html', 'language': None,
                                        'base': 'https://stackoverflow.com/feeds/',
                                        'value': '<p>My function which change '
                                                 'password:</p>\n\n<pre><code>func '
                                                 'changePassword(oldPassword: String, '
                                                 'newPassword: String){\n\n        '
                                                 'AppDelegate.defaultUserPool().currentUser('
                                                 ')?.changePassword(oldPassword, '
                                                 'proposedPassword: newPassword)\n\n\n        '
                                                 'AppDelegate.defaultUserPool().currentUser('
                                                 ')?.clearSession()\n\n\n    '
                                                 '}\n</code></pre>\n\n<p>It works quite well, '
                                                 'but I don\'t know how to catch console '
                                                 'exceptions (for example when I write bad '
                                                 'old password)</p>\n\n<pre><code>Response '
                                                 'body:\n{"__type":"NotAuthorizedException",'
                                                 '"message":"Incorrect username or '
                                                 'password."}\n\n"x-amzn-errormessage" = '
                                                 '"Incorrect username or password.";\n    '
                                                 '"x-amzn-errortype" = '
                                                 '"NotAuthorizedException:";\n</code></pre>\n\n<p>How '
                                                 'handle it all?</p>'}},
                    {'id': 'https://stackoverflow.com/q/59273030', 'guidislink': True,
                     'link':
                         'https://stackoverflow.com/questions/59273030/play-audio-file-in-vuejs'
                         '-application',
                     're_rank': {'scheme': 'https://stackoverflow.com'},
                     'title': 'Play audio file in vuejs application',
                     'title_detail': {'type': 'text/plain', 'language': None,
                                      'base': 'https://stackoverflow.com/feeds/',
                                      'value': 'Play audio file in vuejs application'},
                     'tags': [{'term': 'vue.js', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None},
                              {'term': 'vuejs2', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None},
                              {'term': 'vuetify.js', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None}],
                     'authors': [{'name': 'Rushi', 'href': 'https://stackoverflow.com/users/8401051'}],
                     'author_detail': {'name': 'Rushi',
                                       'href': 'https://stackoverflow.com/users/8401051'},
                     'href': 'https://stackoverflow.com/users/8401051', 'author': 'Rushi',
                     'links': [{'rel': 'alternate',
                                'href':
                                    'https://stackoverflow.com/questions/59273030/play-audio-file-in-vuejs'
                                    '-application',
                                'type': 'text/html'}], 'published': '2019-12-10T18:03:40Z',
                     'updated': '2019-12-10T18:03:40Z',
                     'summary': '<p>I want to play an audio file (mp3,wav) when I click on '
                                'button in vuejs. Can anybody tell me the code or any '
                                'reference library that will work on browser.</p>',
                     'summary_detail': {'type': 'text/html', 'language': None,
                                        'base': 'https://stackoverflow.com/feeds/',
                                        'value': '<p>I want to play an audio file (mp3,'
                                                 'wav) when I click on button in vuejs. Can '
                                                 'anybody tell me the code or any reference '
                                                 'library that will work on browser.</p>'}},
                    {'id': 'https://stackoverflow.com/q/59273028', 'guidislink': True,
                     'link':
                         'https://stackoverflow.com/questions/59273028/is-it-possible-to-work-with'
                         '-google-maps-javascript-api-without-api-key',
                     're_rank': {'scheme': 'https://stackoverflow.com'},
                     'title': 'Is it possible to work with Google Maps JavaScript API without '
                              'API_KEY?',
                     'title_detail': {'type': 'text/plain', 'language': None,
                                      'base': 'https://stackoverflow.com/feeds/',
                                      'value': 'Is it possible to work with Google Maps '
                                               'JavaScript API without API_KEY?'},
                     'tags': [{'term': 'google-maps-api-3',
                               'scheme': 'https://stackoverflow.com/tags', 'label': None}],
                     'authors': [
                         {'name': 'Helen', 'href': 'https://stackoverflow.com/users/11395399'}],
                     'author_detail': {'name': 'Helen',
                                       'href': 'https://stackoverflow.com/users/11395399'},
                     'href': 'https://stackoverflow.com/users/11395399', 'author': 'Helen',
                     'links': [{'rel': 'alternate',
                                'href':
                                    'https://stackoverflow.com/questions/59273028/is-it-possible-to-work-with-google'
                                    '-maps-javascript-api-without-api-key',
                                'type': 'text/html'}], 'published': '2019-12-10T18:02:59Z',
                     'updated': '2019-12-10T18:02:59Z',
                     'summary': '<p>In my project for the university I wanted to use Google '
                                'Maps JavaScript API. For example, I tried to use this '
                                'code.</p>\n\n<pre><code>&lt;!DOCTYPE '
                                'html&gt;\n&lt;html&gt;\n  &lt;head&gt;\n    &lt;meta '
                                'name="viewport" content="initial-scale=1.0, '
                                'user-scalable=no"&gt;\n    &lt;meta charset="utf-8"&gt;\n    '
                                '&lt;title&gt;Simple Marker Icons&lt;/title&gt;\n    '
                                '&lt;style&gt;\n      /* Always set the map height explicitly '
                                'to define the size of the div\n       * element that '
                                'contains the map. */\n      #map {\n        height: 100%;\n  '
                                '    }\n      /* Optional: Makes the sample page fill the '
                                'window. */\n      html, body {\n        height: 100%;\n      '
                                '  margin: 0;\n        padding: 0;\n      }\n    '
                                '&lt;/style&gt;\n  &lt;/head&gt;\n  &lt;body&gt;\n    &lt;div '
                                'id="map"&gt;&lt;/div&gt;\n    &lt;script&gt;\n\n      // '
                                'This example adds a marker to indicate the position of Bondi '
                                'Beach in Sydney,\n      // Australia.\n      function '
                                'initMap() {\n        var map = new google.maps.Map('
                                'document.getElementById(\'map\'), {\n          zoom: 4,'
                                '\n          center: {lat: -33, lng: 151}\n        });\n\n    '
                                '    var image = '
                                '\'https://developers.google.com/maps/documentation/javascript/examples/full/images'
                                '/beachflag.png\';\n        var beachMarker = new google.maps.Marker({\n          '
                                'position: {lat: -33.890, lng: 151.274},\n          map: map,\n          icon: '
                                'image\n        });\n      }\n    &lt;/script&gt;\n    &lt;script async defer\n    '
                                'src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&amp;callback=initMap'
                                '"&gt;\n    &lt;/script&gt;\n  &lt;/body&gt;\n&lt;/html&gt;\n</code></pre>\n\n<p>But '
                                'it did not work without API_KEY. My project is not commercial, it will never be '
                                'posted on a real server and I want to understand if it is possible to work without '
                                'this key? Or maybe it’s worth switching to another product?</p>',
                     'summary_detail': {'type': 'text/html', 'language': None,
                                        'base': 'https://stackoverflow.com/feeds/',
                                        'value': '<p>In my project for the university I wanted to use Google Maps '
                                                 'JavaScript API. For example, I tried to use this '
                                                 'code.</p>\n\n<pre><code>&lt;!DOCTYPE html&gt;\n&lt;html&gt;\n  '
                                                 '&lt;head&gt;\n    &lt;meta name="viewport" '
                                                 'content="initial-scale=1.0, user-scalable=no"&gt;\n    &lt;meta '
                                                 'charset="utf-8"&gt;\n    &lt;title&gt;Simple Marker '
                                                 'Icons&lt;/title&gt;\n    &lt;style&gt;\n      /* Always set the '
                                                 'map height explicitly to define the size of the div\n       * '
                                                 'element that contains the map. */\n'
                                                 '#map {\n        height: 100%;\n      }\n    '
                                                 '  /* Optional: Makes the sample page fill '
                                                 'the window. */\n      html, body {\n        '
                                                 'height: 100%;\n        margin: 0;\n        '
                                                 'padding: 0;\n      }\n    &lt;/style&gt;\n  '
                                                 '&lt;/head&gt;\n  &lt;body&gt;\n    &lt;div '
                                                 'id="map"&gt;&lt;/div&gt;\n    '
                                                 '&lt;script&gt;\n\n      // This example '
                                                 'adds a marker to indicate the position of '
                                                 'Bondi Beach in Sydney,\n      // '
                                                 'Australia.\n      function initMap() {\n    '
                                                 '    var map = new google.maps.Map('
                                                 'document.getElementById(\'map\'), '
                                                 '{\n          zoom: 4,\n          center: {'
                                                 'lat: -33, lng: 151}\n        });\n\n        '
                                                 'var image = '
                                                 '\'https://developers.google.com/maps/documentation/javascript/'
                                                 'examples/full/images/beachflag.png\';\n        var beachMarker = '
                                                 'new google.maps.Marker({\n          position: {lat: -33.890, '
                                                 'lng: 151.274},\n          map: map,\n          icon: image\n       '
                                                 ' });\n      }\n    &lt;/script&gt;\n    &lt;script async defer\n   '
                                                 ' src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&amp;'
                                                 'callback=initMap"&gt;\n    &lt;/script&gt;\n  '
                                                 '&lt;/body&gt;\n&lt;/html&gt;\n</code></pre>\n\n<p>But it did not '
                                                 'work without API_KEY. My project is not commercial, it will never '
                                                 'be posted on a real server and I want to understand if it is '
                                                 'possible to work without this key? Or maybe it’s worth switching '
                                                 'to another product?</p>'}},
                    {'id': 'https://stackoverflow.com/q/59273027', 'guidislink': True,
                     'link':
                         'https://stackoverflow.com/questions/59273027/realted-to-secuirty'
                         '-valunerability-cve-2018-9206-in-the-file-jquery-fileupload-j',
                     're_rank': {'scheme': 'https://stackoverflow.com'},
                     'title': 'Realted to secuirty valunerability CVE-2018-9206 in the file '
                              'jquery.fileupload.js file in DNN 7.3.4 and DNN 9.3',
                     'title_detail': {'type': 'text/plain', 'language': None,
                                      'base': 'https://stackoverflow.com/feeds/',
                                      'value': 'Realted to secuirty valunerability '
                                               'CVE-2018-9206 in the file '
                                               'jquery.fileupload.js file in DNN 7.3.4 and '
                                               'DNN 9.3'},
                     'tags': [{'term': 'dotnetnuke', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None}, {'term': 'dotnetnuke-7',
                                                'scheme': 'https://stackoverflow.com/tags',
                                                'label': None},
                              {'term': 'dnn-module', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None},
                              {'term': 'dnn9', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None}], 'authors': [
                        {'name': 'afzaal', 'href': 'https://stackoverflow.com/users/12513380'}],
                     'author_detail': {'name': 'afzaal',
                                       'href': 'https://stackoverflow.com/users/12513380'},
                     'href': 'https://stackoverflow.com/users/12513380', 'author': 'afzaal',
                     'links': [{'rel': 'alternate',
                                'href':
                                    'https://stackoverflow.com/questions/59273027/realted-to-secuirty-valunerability'
                                    '-cve-2018-9206-in-the-file-jquery-fileupload-j',
                                'type': 'text/html'}], 'published': '2019-12-10T18:02:50Z',
                     'updated': '2019-12-10T18:02:50Z',
                     'summary': '<p>There is a security vulnerability CVE-2018-9206  '
                                'jquery.fileupload.js file \non the following '
                                'path\nresources/shared/scripts/jquery/jquery.fileuploahed.js '
                                '\njquery.fileupload.js is version 5.37.0 (creation Year is '
                                '2010) in our dnn7.3.4 and dnn9.3 environment  </p>\n\n<p>do '
                                'we need to do anything to mitigate/remove the vulnerability '
                                '? also is this file is only accessible  from admin area ?</p>',
                     'summary_detail': {'type': 'text/html', 'language': None,
                                        'base': 'https://stackoverflow.com/feeds/',
                                        'value': '<p>There is a security vulnerability '
                                                 'CVE-2018-9206  jquery.fileupload.js file '
                                                 '\non the following '
                                                 'path\nresources/shared/scripts/jquery/jquery.fileuploahed.js '
                                                 '\njquery.fileupload.js is version 5.37.0 (creation Year is 2010) '
                                                 'in our dnn7.3.4 and dnn9.3 environment  </p>\n\n<p>do we need to '
                                                 'do anything to mitigate/remove the vulnerability ? also is this '
                                                 'file is only accessible  from admin area ?</p>'}},
                    {'id': 'https://stackoverflow.com/q/59273025', 'guidislink': True,
                     'link':
                         'https://stackoverflow.com/questions/59273025/ckeditor-5-cant-change-upload'
                         '-url-after-init',
                     're_rank': {'scheme': 'https://stackoverflow.com'},
                     'title': "CKEditor 5 Can't change upload url after Init",
                     'title_detail': {'type': 'text/plain', 'language': None,
                                      'base': 'https://stackoverflow.com/feeds/',
                                      'value': "CKEditor 5 Can't change upload url after Init"},
                     'tags': [{'term': 'ckeditor', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None},
                              {'term': 'ckfinder', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None}], 'authors': [
                        {'name': 'Armen', 'href': 'https://stackoverflow.com/users/12220647'}],
                     'author_detail': {'name': 'Armen',
                                       'href': 'https://stackoverflow.com/users/12220647'},
                     'href': 'https://stackoverflow.com/users/12220647', 'author': 'Armen',
                     'links': [{'rel': 'alternate',
                                'href':
                                    'https://stackoverflow.com/questions/59273025/ckeditor-5-cant-change-upload-url'
                                    '-after-init',
                                'type': 'text/html'}], 'published': '2019-12-10T18:02:37Z',
                     'updated': '2019-12-10T18:02:37Z',
                     'summary': '<p>I\'m using CKEditor for my project, and for the image '
                                'upload I\'m using '
                                'ckfinder</p>\n\n<pre><code>DecoupledEditor.create( enEditor, '
                                '{\n            ckfinder: {\n                uploadUrl: '
                                '`/news/upload_image?_token=${'
                                'csrfToken}&amp;tmpToken=someToken`,\n            }\n        '
                                '})\n        .then( editor =&gt; {\n            '
                                'document.querySelector( \'.toolbar-container\' '
                                ').appendChild( editor.ui.view.toolbar.element );\n           '
                                ' window.ckEditor = editor;\n        } )\n        .catch( '
                                'error =&gt; {\n            console.error( error );\n        '
                                '} );\n</code></pre>\n\n<p>After some actions I need to '
                                'change upload url\nI\'ve tryed to use setter of '
                                '<code>ckEditor</code>, like this, but it doesn\'t '
                                'helps</p>\n\n<pre><code>ckEditor.config.set("ckfinder", '
                                '{uploadUrl: '
                                '"newUrl"});\n</code></pre>\n\n<p>or</p>\n\n<pre><code>ckEditor.config._config'
                                '.ckfinder.uploadUrl = "newUrl";\n</code></pre>\n\n<p>how I can change uploadUrl of '
                                'ckFinder? Thanks</p>',
                     'summary_detail': {'type': 'text/html', 'language': None,
                                        'base': 'https://stackoverflow.com/feeds/',
                                        'value': '<p>I\'m using CKEditor for my project, '
                                                 'and for the image upload I\'m using '
                                                 'ckfinder</p>\n\n<pre><code>DecoupledEditor.create( '
                                                 'enEditor, {\n            ckfinder: {\n              '
                                                 '  uploadUrl: `/news/upload_image?_token=${'
                                                 'csrfToken}&amp;tmpToken=someToken`,\n            '
                                                 '}\n        })\n        .then( editor =&gt; {\n      '
                                                 '      document.querySelector( '
                                                 '\'.toolbar-container\' ).appendChild( '
                                                 'editor.ui.view.toolbar.element );\n            '
                                                 'window.ckEditor = editor;\n        } )\n        '
                                                 '.catch( error =&gt; {\n            console.error( '
                                                 'error );\n        } );\n</code></pre>\n\n<p>After '
                                                 'some actions I need to change upload url\nI\'ve '
                                                 'tryed to use setter of <code>ckEditor</code>, '
                                                 'like this, but it doesn\'t '
                                                 'helps</p>\n\n<pre><code>ckEditor.config.set('
                                                 '"ckfinder", {uploadUrl: '
                                                 '"newUrl"});\n</code></pre>\n\n<p>or</p>\n\n<pre><code>ckEditor.'
                                                 'config._config.ckfinder.uploadUrl = '
                                                 '"newUrl";\n</code></pre>\n\n<p>how I can change uploadUrl of '
                                                 'ckFinder? Thanks</p>'}},
                    {'id': 'https://stackoverflow.com/q/59273022', 'guidislink': True,
                     'link':
                         'https://stackoverflow.com/questions/59273022/dont-bind-correctly-a-combobox'
                         '-silverlight-5-wpf',
                     're_rank': {'scheme': 'https://stackoverflow.com'},
                     'title': "Don't bind correctly a combobox silverlight 5 WPF",
                     'title_detail': {'type': 'text/plain', 'language': None,
                                      'base': 'https://stackoverflow.com/feeds/',
                                      'value': "Don't bind correctly a combobox silverlight 5 "
                                               "WPF"},
                     'tags': [{'term': 'c#', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None},
                              {'term': 'wpf', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None}, {'term': 'silverlight-5.0',
                                                'scheme': 'https://stackoverflow.com/tags',
                                                'label': None}], 'authors': [
                        {'name': 'ger', 'href': 'https://stackoverflow.com/users/4668184'}],
                     'author_detail': {'name': 'ger',
                                       'href': 'https://stackoverflow.com/users/4668184'},
                     'href': 'https://stackoverflow.com/users/4668184', 'author': 'ger',
                     'links': [{'rel': 'alternate',
                                'href':
                                    'https://stackoverflow.com/questions/59273022/dont-bind-correctly-a-combobox'
                                    '-silverlight-5-wpf',
                                'type': 'text/html'}], 'published': '2019-12-10T18:02:22Z',
                     'updated': '2019-12-10T18:02:22Z',
                     'summary': '<p>I have to add a combo box control in a Silverlight '
                                'application with MVVM Pattern, it does not use '
                                'ObjectDataProvider for bind the control,  instead is use ('
                                'line code) a class converter like '
                                'this:</p>\n\n<pre><code>public class '
                                'EnumToIEnumerableConverter : IValueConverter\n{\n    private '
                                'Dictionary&lt;Type, List&lt;object&gt;&gt; cache = new '
                                'Dictionary&lt;Type, List&lt;object&gt;&gt;();\n\n    public '
                                'object Convert(object value, Type targetType, '
                                'object parameter, System.Globalization.CultureInfo '
                                'culture)\n    {\n        var type = value.GetType();\n       '
                                ' if (!this.cache.ContainsKey(type))\n        {\n            '
                                'var fields = type.GetFields().Where(field =&gt; '
                                'field.IsLiteral);\n            var values = new '
                                'List&lt;object&gt;();\n            if (('
                                'int)fields.ElementAt(0).GetRawConstantValue() &gt; 0)\n      '
                                '      {\n                values.Add(null); \n            }\n '
                                '           foreach (var field in fields)\n            {\n    '
                                '            DescriptionAttribute[] a = ('
                                'DescriptionAttribute[])field.GetCustomAttributes(typeof('
                                'DescriptionAttribute), false);\n                if (a != '
                                'null &amp;&amp; a.Length &gt; 0)\n                    '
                                'values.Add(a[0].Description);\n                else\n        '
                                '            values.Add(field.GetValue(value));\n            '
                                '}\n            this.cache[type] = values;\n        }\n\n     '
                                '   return this.cache[type];\n    }\n</code></pre>\n\n<p>in '
                                'the Model Layer the enum what I\'ve to show in the view... ('
                                'binding the combobox)</p>\n\n<pre><code> public enum TipoPPA '
                                '\n{\n    [Description("SRT")]\n    SRT=1,\n    [Description('
                                '"Conexión")]\n    Conexion=2,\n    [Description('
                                '"Ejecutor")]\n    Ejecutor=1\n}\n</code></pre>\n\n<p>In my '
                                'viewmodel I\'ve defined</p>\n\n<pre><code>        public '
                                'TipoPPA Tipoppa\n    {\n        get\n        {\n            '
                                'return TipoPpa;\n        }\n        set\n        {\n         '
                                '   TipoPpa = value;\n            this.RaisePropertyChanged(('
                                ') =&gt; this.Tipoppa);\n        }\n    '
                                '}\n</code></pre>\n\n<p>and I created a list '
                                '</p>\n\n<pre><code>   private List&lt;TipoPpaTO&gt; '
                                'ListTipoPPA; &lt;== private field\n   public '
                                'List&lt;TipoPpaTO&gt; ListTipoPpa\n    {\n        get\n      '
                                '  {\n            return ListTipoPPA;\n        }\n        '
                                'set\n        {\n            if (ListTipoPPA != value)\n      '
                                '      {\n                ListTipoPPA = value;\n              '
                                '  this.RaisePropertyChanged(() =&gt; this.ListTipoPpa);\n    '
                                '        }\n        }\n    }\n  /// a transfer object\n    '
                                'public class TipoPpaTO\n   {\n    public int IdPPA { get; '
                                'set; }\n\n    public TipoPPA Nombre { get; set; }\n\n    '
                                '}\n</code></pre>\n\n<p>and XAML is binded to '
                                'listTipoppa</p>\n\n<pre><code>            &lt;ComboBox '
                                'Name="ComboTipoPpa" Grid.Row="10" Grid.Column="1"\n          '
                                '        Height="26" Width="177" \n                  '
                                'HorizontalAlignment="Left" \n                  Margin="10,1,'
                                '0,1"\n                  IsEnabled="{Binding '
                                'ElementName=cbAgregarManual, Path=IsChecked}" \n             '
                                '     SelectedItem="{Binding Path=Tipoppa, Mode=TwoWay, '
                                'ValidatesOnNotifyDataErrors=True, Converter={StaticResource '
                                'EnumToIntConverter}}"\n                  ItemsSource="{'
                                'Binding Path=ListTipoPpa, Converter={StaticResource '
                                'EnumToIEnumerableConverter}}"/&gt;\n</code></pre>\n\n<p>When '
                                'I run the app shows me this...</p>\n\n<p><a '
                                'href="https://i.stack.imgur.com/nHiAD.png" rel="nofollow '
                                'noreferrer"><img alt="enter image description here" '
                                'src="https://i.stack.imgur.com/nHiAD.png" '
                                '/></a></p>\n\n<p>what I\'m doing wrong?</p>',
                     'summary_detail': {'type': 'text/html', 'language': None,
                                        'base': 'https://stackoverflow.com/feeds/',
                                        'value': '<p>I have to add a combo box control in a '
                                                 'Silverlight application with MVVM Pattern, '
                                                 'it does not use ObjectDataProvider for bind '
                                                 'the control,  instead is use (line code) a '
                                                 'class converter like '
                                                 'this:</p>\n\n<pre><code>public class '
                                                 'EnumToIEnumerableConverter : '
                                                 'IValueConverter\n{\n    private '
                                                 'Dictionary&lt;Type, List&lt;object&gt;&gt; '
                                                 'cache = new Dictionary&lt;Type, '
                                                 'List&lt;object&gt;&gt;();\n\n    public '
                                                 'object Convert(object value, '
                                                 'Type targetType, object parameter, '
                                                 'System.Globalization.CultureInfo culture)\n '
                                                 '   {\n        var type = value.GetType();\n '
                                                 '       if (!this.cache.ContainsKey(type))\n '
                                                 '       {\n            var fields = '
                                                 'type.GetFields().Where(field =&gt; '
                                                 'field.IsLiteral);\n            var values = '
                                                 'new List&lt;object&gt;();\n            if ('
                                                 '(int)fields.ElementAt('
                                                 '0).GetRawConstantValue() &gt; 0)\n          '
                                                 '  {\n                values.Add(null); \n   '
                                                 '         }\n            foreach (var field '
                                                 'in fields)\n            {\n                '
                                                 'DescriptionAttribute[] a = ('
                                                 'DescriptionAttribute['
                                                 '])field.GetCustomAttributes(typeof('
                                                 'DescriptionAttribute), false);\n            '
                                                 '    if (a != null &amp;&amp; a.Length &gt; '
                                                 '0)\n                    values.Add(a['
                                                 '0].Description);\n                else\n    '
                                                 '                values.Add(field.GetValue('
                                                 'value));\n            }\n            '
                                                 'this.cache[type] = values;\n        }\n\n   '
                                                 '     return this.cache[type];\n    '
                                                 '}\n</code></pre>\n\n<p>in the Model Layer '
                                                 'the enum what I\'ve to show in the view... '
                                                 '(binding the combobox)</p>\n\n<pre><code> '
                                                 'public enum TipoPPA \n{\n    [Description('
                                                 '"SRT")]\n    SRT=1,\n    [Description('
                                                 '"Conexión")]\n    Conexion=2,'
                                                 '\n    [Description("Ejecutor")]\n    '
                                                 'Ejecutor=1\n}\n</code></pre>\n\n<p>In my '
                                                 'viewmodel I\'ve defined</p>\n\n<pre><code>  '
                                                 '      public TipoPPA Tipoppa\n    {\n       '
                                                 ' get\n        {\n            return '
                                                 'TipoPpa;\n        }\n        set\n        {'
                                                 '\n            TipoPpa = value;\n            '
                                                 'this.RaisePropertyChanged(() =&gt; '
                                                 'this.Tipoppa);\n        }\n    '
                                                 '}\n</code></pre>\n\n<p>and I created a list '
                                                 '</p>\n\n<pre><code>   private '
                                                 'List&lt;TipoPpaTO&gt; ListTipoPPA; &lt;== '
                                                 'private field\n   public '
                                                 'List&lt;TipoPpaTO&gt; ListTipoPpa\n    {\n  '
                                                 '      get\n        {\n            return '
                                                 'ListTipoPPA;\n        }\n        set\n      '
                                                 '  {\n            if (ListTipoPPA != '
                                                 'value)\n            {\n                '
                                                 'ListTipoPPA = value;\n                '
                                                 'this.RaisePropertyChanged(() =&gt; '
                                                 'this.ListTipoPpa);\n            }\n        '
                                                 '}\n    }\n  /// a transfer object\n    '
                                                 'public class TipoPpaTO\n   {\n    public '
                                                 'int IdPPA { get; set; }\n\n    public '
                                                 'TipoPPA Nombre { get; set; }\n\n    '
                                                 '}\n</code></pre>\n\n<p>and XAML is binded '
                                                 'to listTipoppa</p>\n\n<pre><code>           '
                                                 ' &lt;ComboBox Name="ComboTipoPpa" '
                                                 'Grid.Row="10" Grid.Column="1"\n             '
                                                 '     Height="26" Width="177" \n             '
                                                 '     HorizontalAlignment="Left" \n          '
                                                 '        Margin="10,1,0,1"\n                 '
                                                 ' IsEnabled="{Binding '
                                                 'ElementName=cbAgregarManual, '
                                                 'Path=IsChecked}" \n                  '
                                                 'SelectedItem="{Binding Path=Tipoppa, '
                                                 'Mode=TwoWay, '
                                                 'ValidatesOnNotifyDataErrors=True, '
                                                 'Converter={StaticResource '
                                                 'EnumToIntConverter}}"\n                  '
                                                 'ItemsSource="{Binding Path=ListTipoPpa, '
                                                 'Converter={StaticResource '
                                                 'EnumToIEnumerableConverter}}"/&gt;\n</code></pre>\n\n<p>When I run '
                                                 'the app shows me this...</p>\n\n<p><a '
                                                 'href="https://i.stack.imgur.com/nHiAD.png" rel="nofollow '
                                                 'noreferrer"><img alt="enter image description here" '
                                                 'src="https://i.stack.imgur.com/nHiAD.png" /></a></p>\n\n<p>what '
                                                 'I\'m doing wrong?</p>'}},
                    {'id': 'https://stackoverflow.com/q/59272985', 'guidislink': True,
                     'link':
                         'https://stackoverflow.com/questions/59272985/resize-log-file-database-sql'
                         '-server-on-docker',
                     're_rank': {'scheme': 'https://stackoverflow.com'},
                     'title': 'Resize log file Database sql server on docker',
                     'title_detail': {'type': 'text/plain', 'language': None,
                                      'base': 'https://stackoverflow.com/feeds/',
                                      'value': 'Resize log file Database sql server on docker'},
                     'tags': [{'term': 'sql', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None},
                              {'term': 'sql-server', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None},
                              {'term': 'docker', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None}], 'authors': [
                        {'name': 'Riki', 'href': 'https://stackoverflow.com/users/12347516'}],
                     'author_detail': {'name': 'Riki',
                                       'href': 'https://stackoverflow.com/users/12347516'},
                     'href': 'https://stackoverflow.com/users/12347516', 'author': 'Riki',
                     'links': [{'rel': 'alternate',
                                'href':
                                    'https://stackoverflow.com/questions/59272985/resize-log-file-database-sql'
                                    '-server-on-docker',
                                'type': 'text/html'}], 'published': '2019-12-10T18:00:12Z',
                     'updated': '2019-12-10T18:02:36Z',
                     'summary': "<p>i have sql-server 2017 on docker I have to change the "
                                "size of the log file, but when I run the sql command below I "
                                "have the following error, how do I solve "
                                "this?</p>\n\n<p><strong>Error: MODIFY FILE encountered "
                                "operating system error 31(A device attached to the system is "
                                "not functioning.) while attempting to expand the physical "
                                "file '\\var\\opt\\mssql\\data\\MYDB_log.ldf'</strong> "
                                "</p>\n\n<p><strong>SQL "
                                "QUERY</strong></p>\n\n<pre><code>ALTER DATABASE MYDB\nMODIFY "
                                "FILE\n(NAME = MYDB_log,\nSIZE = 1500MB);\n</code></pre>",
                     'summary_detail': {'type': 'text/html', 'language': None,
                                        'base': 'https://stackoverflow.com/feeds/',
                                        'value': "<p>i have sql-server 2017 on docker I have "
                                                 "to change the size of the log file, "
                                                 "but when I run the sql command below I have "
                                                 "the following error, how do I solve "
                                                 "this?</p>\n\n<p><strong>Error: MODIFY FILE "
                                                 "encountered operating system error 31(A "
                                                 "device attached to the system is not "
                                                 "functioning.) while attempting to expand "
                                                 "the physical file "
                                                 "'\\var\\opt\\mssql\\data\\MYDB_log.ldf'</strong> "
                                                 "</p>\n\n<p><strong>SQL "
                                                 "QUERY</strong></p>\n\n<pre><code>ALTER DATABASE "
                                                 "MYDB\nMODIFY FILE\n(NAME = MYDB_log,"
                                                 "\nSIZE = 1500MB);\n</code></pre>"}},
                    {'id': 'https://stackoverflow.com/q/59272973', 'guidislink': True,
                     'link':
                         'https://stackoverflow.com/questions/59272973/how-to-setup-multiple-spring'
                         '-data-jpa-with-different-base-packages-transactionma',
                     're_rank': {'scheme': 'https://stackoverflow.com'},
                     'title': 'How to setup multiple Spring Data JPA with different '
                              'base-packages,transactionManagerRef using class based '
                              'configuration?',
                     'title_detail': {'type': 'text/plain', 'language': None,
                                      'base': 'https://stackoverflow.com/feeds/',
                                      'value': 'How to setup multiple Spring Data JPA with '
                                               'different base-packages,transactionManagerRef '
                                               'using class based configuration?'},
                     'tags': [{'term': 'java', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None},
                              {'term': 'spring', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None}, {'term': 'spring-data-jpa',
                                                'scheme': 'https://stackoverflow.com/tags',
                                                'label': None}, {'term': 'spring-data',
                                                                 'scheme':
                                                                     'https://stackoverflow.com/tags',
                                                                 'label': None}], 'authors': [
                        {'name': 'Ram', 'href': 'https://stackoverflow.com/users/7434767'}],
                     'author_detail': {'name': 'Ram',
                                       'href': 'https://stackoverflow.com/users/7434767'},
                     'href': 'https://stackoverflow.com/users/7434767', 'author': 'Ram',
                     'links': [{'rel': 'alternate',
                                'href':
                                    'https://stackoverflow.com/questions/59272973/how-to-setup-multiple-spring-data'
                                    '-jpa-with-different-base-packages-transactionma',
                                'type': 'text/html'}], 'published': '2019-12-10T17:59:21Z',
                     'updated': '2019-12-10T18:03:07Z',
                     'summary': '<p>In our current XML based configuration, we have setup for '
                                'multiple repositories like below:</p>\n\n<pre><code>    '
                                '&lt;jpa:repositories '
                                'base-package="com.grc.riskanalysis.repository.master" '
                                'transaction-manager-ref="transactionManager"\n               '
                                '   entity-manager-factory-ref="entityManagerFactory"/&gt;\n  '
                                '  &lt;jpa:repositories '
                                'base-package="com.grc.riskanalysis.repository.slave" '
                                'transaction-manager-ref="transactionManager2"\n              '
                                '    '
                                'entity-manager-factory-ref="dynamicEntityManagerFactory"/&gt;\n</code></pre>\n\n<p'
                                '>I am trying to migrate this XML configuration to class based configuration, '
                                'but it is not allowing to have multiple @EnableJpaRepositories annotations. How to '
                                'achieve this with class based (annotation based) configuration ? </p>',
                     'summary_detail': {'type': 'text/html', 'language': None,
                                        'base': 'https://stackoverflow.com/feeds/',
                                        'value': '<p>In our current XML based configuration, '
                                                 'we have setup for multiple repositories '
                                                 'like below:</p>\n\n<pre><code>    '
                                                 '&lt;jpa:repositories '
                                                 'base-package="com.grc.riskanalysis.repository.master" '
                                                 'transaction-manager-ref="transactionManager"\n                  '
                                                 'entity-manager-factory-ref="entityManagerFactory"/&gt;\n    '
                                                 '&lt;jpa:repositories '
                                                 'base-package="com.grc.riskanalysis.repository.slave" '
                                                 'transaction-manager-ref="transactionManager2"\n                  '
                                                 'entity-manager-factory-ref="dynamicEntityManagerFactory"/&gt;\n'
                                                 '</code></pre>\n\n<p>I am trying to migrate this XML configuration '
                                                 'to class based configuration, but it is not allowing to have '
                                                 'multiple @EnableJpaRepositories annotations. How to achieve this '
                                                 'with class based (annotation based) configuration ? </p>'}},
                    {'id': 'https://stackoverflow.com/q/59272964', 'guidislink': True,
                     'link':
                         'https://stackoverflow.com/questions/59272964/pivot-on-specific-columns-in'
                         '-pandas-dataframe',
                     're_rank': {'scheme': 'https://stackoverflow.com'},
                     'title': 'Pivot on specific columns in pandas dataframe',
                     'title_detail': {'type': 'text/plain', 'language': None,
                                      'base': 'https://stackoverflow.com/feeds/',
                                      'value': 'Pivot on specific columns in pandas dataframe'},
                     'tags': [{'term': 'pandas', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None},
                              {'term': 'dataframe', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None}], 'authors': [
                        {'name': 'soling', 'href': 'https://stackoverflow.com/users/4212055'}],
                     'author_detail': {'name': 'soling',
                                       'href': 'https://stackoverflow.com/users/4212055'},
                     'href': 'https://stackoverflow.com/users/4212055', 'author': 'soling',
                     'links': [{'rel': 'alternate',
                                'href':
                                    'https://stackoverflow.com/questions/59272964/pivot-on-specific-columns-in'
                                    '-pandas-dataframe',
                                'type': 'text/html'}], 'published': '2019-12-10T17:58:26Z',
                     'updated': '2019-12-10T18:04:30Z',
                     'summary': "<p>I would like to apply a type of pivot on a pandas "
                                "dataframe but I can't find the proper way to do "
                                "it.</p>\n\n<p>What I want to "
                                "do:</p>\n\n<p><code>input_df</code>:</p>\n\n<pre><code>p_id "
                                "p_name prod_t1 prod_t2 "
                                "prod_t3\n-----------------------------------\n1    foo    3  "
                                "     2       4\n2    bar    0       1       "
                                "0\n</code></pre>\n\n<p><code>expected_output_df</code>:</p>\n\n<pre><code>p_id "
                                "p_name prod_time quantity\n-----------------------------------\n1    foo    prod_t1 "
                                "  3\n1    foo    prod_t2   2\n1    foo    prod_t3   4\n2    bar    prod_t1   0\n2   "
                                " bar    prod_t2   1\n2    bar    prod_t3   0\n</code></pre>",
                     'summary_detail': {'type': 'text/html', 'language': None,
                                        'base': 'https://stackoverflow.com/feeds/',
                                        'value': "<p>I would like to apply a type of pivot on "
                                                 "a pandas dataframe but I can't find the "
                                                 "proper way to do it.</p>\n\n<p>What I want "
                                                 "to "
                                                 "do:</p>\n\n<p><code>input_df</code>:</p>\n\n<pre><code>p_id p_name "
                                                 "prod_t1 prod_t2 prod_t3\n-----------------------------------\n1    "
                                                 "foo    3       2       4\n2    bar    0       1       "
                                                 "0\n</code></pre>\n\n<p><code>expected_output_df</code>:</p>\n\n<pre>"
                                                 "<code>p_id p_name prod_time "
                                                 "quantity\n-----------------------------------\n1    foo    prod_t1 "
                                                 "  3\n1    foo    prod_t2   2\n1    foo    prod_t3   4\n2    bar    "
                                                 "prod_t1   0\n2    bar    prod_t2   1\n2    bar    prod_t3   "
                                                 "0\n</code></pre>"}},
                    {'id': 'https://stackoverflow.com/q/59272955', 'guidislink': True,
                     'link':
                         'https://stackoverflow.com/questions/59272955/what-is-wrong-with-the-rename'
                         '-rename-function-after-copy-image-copy-to-new-f',
                     're_rank': {'scheme': 'https://stackoverflow.com'},
                     'title': 'what is wrong with the rename (rename) function after copy '
                              'image (copy) to new folder (mkdir) [duplicate]',
                     'title_detail': {'type': 'text/plain', 'language': None,
                                      'base': 'https://stackoverflow.com/feeds/',
                                      'value': 'what is wrong with the rename (rename) '
                                               'function after copy image (copy) to new '
                                               'folder (mkdir) [duplicate]'},
                     'tags': [{'term': 'php', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None},
                              {'term': 'mkdir', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None}], 'authors': [{'name': 'user82927',
                                                             'href':
                                                                 'https://stackoverflow.com/users/12512745'}],
                     'author_detail': {'name': 'user82927',
                                       'href': 'https://stackoverflow.com/users/12512745'},
                     'href': 'https://stackoverflow.com/users/12512745', 'author': 'user82927',
                     'links': [{'rel': 'alternate',
                                'href':
                                    'https://stackoverflow.com/questions/59272955/what-is-wrong-with-the-rename'
                                    '-rename-function-after-copy-image-copy-to-new-f',
                                'type': 'text/html'}], 'published': '2019-12-10T17:57:38Z',
                     'updated': '2019-12-10T18:03:38Z',
                     'summary': '<div class="question-status '
                                'question-originals-of-duplicate">\n    <p>This question '
                                'already has an answer here:</p>\n    <ul>\n        <li>\n    '
                                '        <a dir="ltr" '
                                'href="https://stackoverflow.com/questions/12649245/php-why-single-quoted-variables'
                                '-inside-doubles-are-still-parsed">PHP - Why single-quoted variables inside doubles '
                                'are still parsed</a>\n                <span '
                                'class="question-originals-answer-count">\n                    4 answers\n           '
                                '     </span>\n        </li>\n        <li>\n            <a dir="ltr" '
                                'href="https://stackoverflow.com/questions/18357786/single-quotes-and-double-quotes'
                                '-in-php">single quotes and double quotes in php?</a>\n                <span '
                                'class="question-originals-answer-count">\n                    6 answers\n           '
                                '     </span>\n        </li>\n        <li>\n            <a dir="ltr" '
                                'href="https://stackoverflow.com/questions/6670879/can-i-echo-a-variable-with-single'
                                '-quotes">Can I echo a variable with single quotes?</a>\n                <span '
                                'class="question-originals-answer-count">\n                    10 answers\n          '
                                '      </span>\n        </li>\n    </ul>\n    </div>\n\n            <p>i create a '
                                'new folder and copy a image to this new folder by php.\nafter i want to rename it '
                                'with a timestamp.\nit works only up to the rename function.\nAs the result it '
                                'created the folder and made a copy of the image.\nOnly the rename function is not '
                                'working (last line)</p>\n\n<pre><code>$username=$rs-&gt;row[\'id\'];\n//Year in '
                                'YYYY format.\n$year = date("Y");\n//Month in mm format, with leading zeros.\n$month '
                                '= date("m");\n//Day in dd format, with leading zeros.\n$day = date("d");\n//The '
                                'folder path for our file should be YYYY/MM/DD\n$directory = '
                                '"$year$month$day";\n$url = \'http://example.com/members/leer/leer.png\';\n$dir = '
                                '__DIR__ . "/leer/$username"; // Full Path\n$name = \'leer.png\';\nis_dir($dir) || '
                                '@mkdir($dir) || die("Can\'t Create folder");\ncopy($url, $dir . DIRECTORY_SEPARATOR '
                                '. $name);\nrename(\'/leer/$username/leer.png\', '
                                '\'/leer/$username/leer$directory.png\');\n</code></pre>\n\n<p>result: '
                                'example.com/members/leer/1198/leer.png</p>',
                     'summary_detail': {'type': 'text/html', 'language': None,
                                        'base': 'https://stackoverflow.com/feeds/',
                                        'value': '<div class="question-status '
                                                 'question-originals-of-duplicate">\n    '
                                                 '<p>This question already has an answer '
                                                 'here:</p>\n    <ul>\n        <li>\n         '
                                                 '   <a dir="ltr" '
                                                 'href="https://stackoverflow.com/questions/12649245/php-why-single-'
                                                 'quoted-variables-inside-doubles-are-still-parsed">PHP - Why '
                                                 'single-quoted variables inside doubles are still parsed</a>\n      '
                                                 '          <span class="question-originals-answer-count">\n         '
                                                 '           4 answers\n                </span>\n        </li>\n     '
                                                 '   <li>\n            <a dir="ltr" '
                                                 'href="https://stackoverflow.com/questions/18357786/single-quotes-and'
                                                 '-double-quotes-in-php">single quotes and double quotes in '
                                                 'php?</a>\n                <span '
                                                 'class="question-originals-answer-count">\n                    6 '
                                                 'answers\n                </span>\n        </li>\n        <li>\n    '
                                                 '        <a dir="ltr" '
                                                 'href="https://stackoverflow.com/questions/6670879/can-i-echo-a-'
                                                 'variable-with-single-quotes">Can I echo a variable with single '
                                                 'quotes?</a>\n                <span '
                                                 'class="question-originals-answer-count">\n                    10 '
                                                 'answers\n                </span>\n        </li>\n    </ul>\n    '
                                                 '</div>\n\n            <p>i create a new folder and copy a image to '
                                                 'this new folder by php.\nafter i want to rename it with a '
                                                 'timestamp.\nit works only up to the rename function.\nAs the '
                                                 'result it created the folder and made a copy of the image.\nOnly '
                                                 'the rename function is not working (last '
                                                 'line)</p>\n\n<pre><code>$username=$rs-&gt;row[\'id\'];\n//Year in '
                                                 'YYYY format.\n$year = date("Y");\n//Month in mm format, '
                                                 'with leading zeros.\n$month = date("m");\n//Day in dd format, '
                                                 'with leading zeros.\n$day = date("d");\n//The folder path for our '
                                                 'file should be YYYY/MM/DD\n$directory = "$year$month$day";\n$url = '
                                                 '\'http://example.com/members/leer/leer.png\';\n$dir = __DIR__ . '
                                                 '"/leer/$username"; // Full Path\n$name = \'leer.png\';\nis_dir('
                                                 '$dir) || @mkdir($dir) || die("Can\'t Create folder");\ncopy($url, '
                                                 '$dir . DIRECTORY_SEPARATOR . $name);\nrename('
                                                 '\'/leer/$username/leer.png\', '
                                                 '\'/leer/$username/leer$directory.png\');\n</code></pre>\n\n<p>result:'
                                                 ' example.com/members/leer/1198/leer.png</p>'}},
                    {'id': 'https://stackoverflow.com/q/59272920', 'guidislink': True,
                     'link':
                         'https://stackoverflow.com/questions/59272920/cannot-reference-an-identifier'
                         '-before-its-definition-undefine-a',
                     're_rank': {'scheme': 'https://stackoverflow.com'},
                     'title': 'Cannot reference an identifier before its definition: Undefine '
                              'a',
                     'title_detail': {'type': 'text/plain', 'language': None,
                                      'base': 'https://stackoverflow.com/feeds/',
                                      'value': 'Cannot reference an identifier before its '
                                               'definition: Undefine a'},
                     'tags': [{'term': 'racket', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None}], 'authors': [{'name': 'mamus onomas',
                                                             'href':
                                                                 'https://stackoverflow.com/users/12513291'}],
                     'author_detail': {'name': 'mamus onomas',
                                       'href': 'https://stackoverflow.com/users/12513291'},
                     'href': 'https://stackoverflow.com/users/12513291',
                     'author': 'mamus onomas',
                     'links': [{'rel': 'alternate',
                                'href': 'https://stackoverflow.com/questions/59272920/cannot-reference-an-identifier'
                                        '-before-its-definition-undefine-a',
                                'type': 'text/html'}],
                     'published': '2019-12-10T17:55:11Z',
                     'updated': '2019-12-10T18:03:30Z',
                     'summary': '<p>Am Using R5RS it keeps giving error a: undefined; cannot '
                                'reference an identifier before its '
                                'definition.</p>\n\n<p><img alt="enter image description '
                                'here" src="https://i.stack.imgur.com/sY1i9.png" /></p>',
                     'summary_detail': {'type': 'text/html', 'language': None,
                                        'base': 'https://stackoverflow.com/feeds/',
                                        'value': '<p>Am Using R5RS it keeps giving error a: '
                                                 'undefined; cannot reference an identifier '
                                                 'before its definition.</p>\n\n<p><img '
                                                 'alt="enter image description here" '
                                                 'src="https://i.stack.imgur.com/sY1i9.png" '
                                                 '/></p>'}},
                    {'id': 'https://stackoverflow.com/q/59272887', 'guidislink': True,
                     'link':
                         'https://stackoverflow.com/questions/59272887/gstreamer-pipeline-with-udpsrc'
                         '-displaying-and-saving-to-file',
                     're_rank': {'scheme': 'https://stackoverflow.com'},
                     'title': 'GStreamer Pipeline with udpsrc displaying and saving to file',
                     'title_detail': {'type': 'text/plain', 'language': None,
                                      'base': 'https://stackoverflow.com/feeds/',
                                      'value': 'GStreamer Pipeline with udpsrc displaying and '
                                               'saving to file'},
                     'tags': [{'term': 'gstreamer', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None}, {'term': 'gstreamer-1.0',
                                                'scheme': 'https://stackoverflow.com/tags',
                                                'label': None}], 'authors': [
                        {'name': 'Tomaz Canabrava',
                         'href': 'https://stackoverflow.com/users/1077785'}],
                     'author_detail': {'name': 'Tomaz Canabrava',
                                       'href': 'https://stackoverflow.com/users/1077785'},
                     'href': 'https://stackoverflow.com/users/1077785',
                     'author': 'Tomaz Canabrava',
                     'links': [{'rel': 'alternate',
                                'href': 'https://stackoverflow.com/questions/59272887/gstreamer-pipeline-with-udpsrc'
                                        '-displaying-and-saving-to-file',
                                'type': 'text/html'}],
                     'published': '2019-12-10T17:53:08Z',
                     'updated': '2019-12-10T18:02:34Z',
                     'summary': "<p>I'm having a hardtime understanding how to build "
                                "gstreamer pipelines. I'v read many questions on google and "
                                "on stackoverflow that are quite similar to mine, but most of "
                                "them assumes that I know what I'm doing, which is not the "
                                "case.</p>\n\n<p>I am reading the documentation but reading "
                                "the documentation and producing a working pipeline seems to "
                                "be quite different things, and mines are "
                                "failing.</p>\n\n<p>I'm sending this pipeline with "
                                "gst-launch-1.0:</p>\n\n<pre><code>gst-launch-1.0 "
                                "videotestsrc  ! video/x-raw,width=640,height=480 ! \\\n    "
                                "videoconvert ! x264enc ! rtph264pay ! udpsink host=127.0.0.1 "
                                "port=5600\n</code></pre>\n\n<p>and I'm trying to display and "
                                "record the pipeline from within a C application, "
                                "using gst_parse_launch, using this "
                                "pipeline:</p>\n\n<pre><code>udpsrc port=5600 ! "
                                "application/x-rtp, clock-rate=90000,payload=96 \\\n  ! "
                                "rtph264depay ! video/x-h264 ! queue ! h264parse !\n    tee "
                                "name=qgc\n    qgc. ! queue ! decodebin ! glupload ! "
                                "glcolorconvert ! qmlglsink name=sink\n    qgc. ! queue ! "
                                "mp4mux ! filesink "
                                "location=bleh.mp4\n</code></pre>\n\n<p>This pipeline "
                                "correctly displays video but the resulting file is "
                                "completely empty in the disk.</p>\n\n<p>Because there's a "
                                "lot of Gstreamer questions that are quite similar, "
                                "I want to make a few questions to help me not ask questions "
                                "about it in the future.</p>\n\n<p>0 - Is the pipeline "
                                "written properly? the tee's are a bit strange to reference "
                                "and I'm not sure if I used them correctly.</p>\n\n<p>1 - how "
                                "can I discover what's wrong within the pipeline? Is there "
                                "any kind of debugger that I can use to paste a pipeline and "
                                "have a <code>pipeline compiler</code> tell me if things are "
                                "as they should - or at least if there are obvious flaws in "
                                "the pipeline I created (like missing caps or incompatible "
                                "ports)</p>\n\n<p>2 - how would I fix this pipeline to "
                                "receive the video (that plays correctly) and save it in "
                                "disk? I'm pretty sure is something simple but I haven't "
                                "figured it out.</p>\n\n<p>The other answers for similar "
                                "questions are mostly dropping a pipeline that works in the "
                                "user's ccomputer but in a old version of gstreamer, "
                                "that does not work today anymore.\nSorry about the long "
                                "text, I'm exausted.</p>\n\n<p>Happy Christmas.</p>",
                     'summary_detail': {'type': 'text/html', 'language': None,
                                        'base': 'https://stackoverflow.com/feeds/',
                                        'value': "<p>I'm having a hardtime understanding how "
                                                 "to build gstreamer pipelines. I'v read many "
                                                 "questions on google and on stackoverflow "
                                                 "that are quite similar to mine, but most of "
                                                 "them assumes that I know what I'm doing, "
                                                 "which is not the case.</p>\n\n<p>I am "
                                                 "reading the documentation but reading the "
                                                 "documentation and producing a working "
                                                 "pipeline seems to be quite different "
                                                 "things, and mines are "
                                                 "failing.</p>\n\n<p>I'm sending this "
                                                 "pipeline with "
                                                 "gst-launch-1.0:</p>\n\n<pre><code>gst-launch-1.0 "
                                                 "videotestsrc  ! video/x-raw,width=640,height=480 ! "
                                                 "\\\n    videoconvert ! x264enc ! rtph264pay ! "
                                                 "udpsink host=127.0.0.1 "
                                                 "port=5600\n</code></pre>\n\n<p>and I'm trying to "
                                                 "display and record the pipeline from within a C "
                                                 "application, using gst_parse_launch, using this "
                                                 "pipeline:</p>\n\n<pre><code>udpsrc port=5600 ! "
                                                 "application/x-rtp, clock-rate=90000,payload=96 \\\n "
                                                 " ! rtph264depay ! video/x-h264 ! queue ! h264parse "
                                                 "!\n    tee name=qgc\n    qgc. ! queue ! decodebin ! "
                                                 "glupload ! glcolorconvert ! qmlglsink name=sink\n   "
                                                 " qgc. ! queue ! mp4mux ! filesink "
                                                 "location=bleh.mp4\n</code></pre>\n\n<p>This "
                                                 "pipeline correctly displays video but the resulting "
                                                 "file is completely empty in the "
                                                 "disk.</p>\n\n<p>Because there's a lot of Gstreamer "
                                                 "questions that are quite similar, I want to make a "
                                                 "few questions to help me not ask questions about it "
                                                 "in the future.</p>\n\n<p>0 - Is the pipeline "
                                                 "written properly? the tee's are a bit strange to "
                                                 "reference and I'm not sure if I used them "
                                                 "correctly.</p>\n\n<p>1 - how can I discover what's "
                                                 "wrong within the pipeline? Is there any kind of "
                                                 "debugger that I can use to paste a pipeline and "
                                                 "have a <code>pipeline compiler</code> tell me if "
                                                 "things are as they should - or at least if there "
                                                 "are obvious flaws in the pipeline I created (like "
                                                 "missing caps or incompatible ports)</p>\n\n<p>2 - "
                                                 "how would I fix this pipeline to receive the video "
                                                 "(that plays correctly) and save it in disk? I'm "
                                                 "pretty sure is something simple but I haven't "
                                                 "figured it out.</p>\n\n<p>The other answers for "
                                                 "similar questions are mostly dropping a pipeline "
                                                 "that works in the user's ccomputer but in a old "
                                                 "version of gstreamer, that does not work today "
                                                 "anymore.\nSorry about the long text, "
                                                 "I'm exausted.</p>\n\n<p>Happy Christmas.</p>"}},
                    {'id': 'https://stackoverflow.com/q/59272752', 'guidislink': True,
                     'link':
                         'https://stackoverflow.com/questions/59272752/how-to-write-something-below'
                         '-the-css-flexbox',
                     're_rank': {'scheme': 'https://stackoverflow.com'},
                     'title': 'How to write something below the css flexbox',
                     'title_detail': {'type': 'text/plain', 'language': None,
                                      'base': 'https://stackoverflow.com/feeds/',
                                      'value': 'How to write something below the css flexbox'},
                     'tags': [{'term': 'javascript', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None},
                              {'term': 'html', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None},
                              {'term': 'css', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None}], 'authors': [
                        {'name': 'Gaurav', 'href': 'https://stackoverflow.com/users/12420363'}],
                     'author_detail': {'name': 'Gaurav',
                                       'href': 'https://stackoverflow.com/users/12420363'},
                     'href': 'https://stackoverflow.com/users/12420363', 'author': 'Gaurav',
                     'links': [{'rel': 'alternate',
                                'href':
                                    'https://stackoverflow.com/questions/59272752/how-to-write-something-below-the'
                                    '-css-flexbox',
                                'type': 'text/html'}], 'published': '2019-12-10T17:42:28Z',
                     'updated': '2019-12-10T18:02:37Z',
                     'summary': '<p>I am trying to do something like screenshots <a '
                                'href="https://i.stack.imgur.com/JvJe8.png" rel="nofollow '
                                'noreferrer"><img alt="screenshot" '
                                'src="https://i.stack.imgur.com/JvJe8.png" /></a> \nyou can '
                                'see the boxes with name in screenshots. In my code I created '
                                'the boxes but I want the boxes name below each '
                                'boxes.\nPlease give me some hints how to achieve '
                                'it?</p>\n\n<p><div class="snippet">\n<div '
                                'class="snippet-code">\n<pre class="snippet-code-css lang-css '
                                'prettyprint-override"><code>.flex-container {\n  display: '
                                'flex;\n  flex-wrap: nowrap;\n  background-color: '
                                'DodgerBlue;\n}\n\n.flex-container &gt; div {\n  '
                                'background-color: #f1f1f1;\n  width: 100px;\n  margin: '
                                '10px;\n  text-align: center;\n  line-height: 75px;\n  '
                                'font-size: 30px;\n}</code></pre>\n<pre '
                                'class="snippet-code-html lang-html '
                                'prettyprint-override"><code>&lt;!DOCTYPE '
                                'html&gt;\n&lt;html&gt;\n&lt;head&gt;\n&lt;/head&gt;\n&lt;body&gt;\n&lt;h1&gt'
                                ';Flexible Boxes&lt;/h1&gt;\n\n&lt;div class="flex-container"&gt;\n  '
                                '&lt;div&gt;1&lt;/div&gt;&lt;p&gt;box 1&lt;/p&gt;\n  '
                                '&lt;div&gt;2&lt;/div&gt;&lt;p&gt;box 2&lt;/p&gt;\n  '
                                '&lt;div&gt;3&lt;/div&gt;&lt;p&gt;box 3&lt;/p&gt;  \n  '
                                '&lt;div&gt;4&lt;/div&gt;&lt;p&gt;box 4&lt;/p&gt;\n  '
                                '&lt;div&gt;5&lt;/div&gt;&lt;p&gt;box 5&lt;/p&gt;\n  '
                                '&lt;div&gt;6&lt;/div&gt;&lt;p&gt;box 6&lt;/p&gt;  \n  '
                                '&lt;div&gt;7&lt;/div&gt;&lt;p&gt;box 7&lt;/p&gt;\n  '
                                '&lt;div&gt;8&lt;/div&gt;&lt;p&gt;box '
                                '8&lt;/p&gt;\n&lt;/div&gt;\n&lt;/body&gt;\n&lt;/html&gt;</code></pre>\n</div>\n</div'
                                '>\n</p>',
                     'summary_detail': {'type': 'text/html', 'language': None,
                                        'base': 'https://stackoverflow.com/feeds/',
                                        'value': '<p>I am trying to do something like '
                                                 'screenshots <a '
                                                 'href="https://i.stack.imgur.com/JvJe8.png" '
                                                 'rel="nofollow noreferrer"><img '
                                                 'alt="screenshot" '
                                                 'src="https://i.stack.imgur.com/JvJe8.png" '
                                                 '/></a> \nyou can see the boxes with name in '
                                                 'screenshots. In my code I created the boxes '
                                                 'but I want the boxes name below each '
                                                 'boxes.\nPlease give me some hints how to '
                                                 'achieve it?</p>\n\n<p><div '
                                                 'class="snippet">\n<div '
                                                 'class="snippet-code">\n<pre '
                                                 'class="snippet-code-css lang-css '
                                                 'prettyprint-override"><code>.flex-container '
                                                 '{\n  display: flex;\n  flex-wrap: nowrap;\n '
                                                 ' background-color: '
                                                 'DodgerBlue;\n}\n\n.flex-container &gt; div '
                                                 '{\n  background-color: #f1f1f1;\n  width: '
                                                 '100px;\n  margin: 10px;\n  text-align: '
                                                 'center;\n  line-height: 75px;\n  font-size: '
                                                 '30px;\n}</code></pre>\n<pre '
                                                 'class="snippet-code-html lang-html '
                                                 'prettyprint-override"><code>&lt;!DOCTYPE '
                                                 'html&gt;\n&lt;html&gt;\n&lt;head&gt;\n&lt;/head&gt;\n&lt;body&gt;\n'
                                                 '&lt;h1&gt;Flexible Boxes&lt;/h1&gt;\n\n&lt;div '
                                                 'class="flex-container"&gt;\n  &lt;div&gt;1&lt;/div&gt;&lt;p&gt;box '
                                                 '1&lt;/p&gt;\n  &lt;div&gt;2&lt;/div&gt;&lt;p&gt;box 2&lt;/p&gt;\n  '
                                                 '&lt;div&gt;3&lt;/div&gt;&lt;p&gt;box 3&lt;/p&gt;  \n  '
                                                 '&lt;div&gt;4&lt;/div&gt;&lt;p&gt;box 4&lt;/p&gt;\n  '
                                                 '&lt;div&gt;5&lt;/div&gt;&lt;p&gt;box 5&lt;/p&gt;\n  '
                                                 '&lt;div&gt;6&lt;/div&gt;&lt;p&gt;box 6&lt;/p&gt;  \n  '
                                                 '&lt;div&gt;7&lt;/div&gt;&lt;p&gt;box 7&lt;/p&gt;\n  '
                                                 '&lt;div&gt;8&lt;/div&gt;&lt;p&gt;box '
                                                 '8&lt;/p&gt;\n&lt;/div&gt;\n&lt;/body&gt;\n&lt;/html&gt;</code></pre>'
                                                 '\n</div>\n</div>\n</p>'}},
                    {'id': 'https://stackoverflow.com/q/59272727', 'guidislink': True,
                     'link':
                         'https://stackoverflow.com/questions/59272727/bash-exponentiation-limit',
                     're_rank': {'scheme': 'https://stackoverflow.com'},
                     'title': 'Bash exponentiation limit',
                     'title_detail': {'type': 'text/plain', 'language': None,
                                      'base': 'https://stackoverflow.com/feeds/',
                                      'value': 'Bash exponentiation limit'}, 'tags': [
                        {'term': 'bash', 'scheme': 'https://stackoverflow.com/tags',
                         'label': None},
                        {'term': 'exponential', 'scheme': 'https://stackoverflow.com/tags',
                         'label': None}], 'authors': [{'name': 'Сергей Хвощевский',
                                                       'href':
                                                           'https://stackoverflow.com/users/9497567'}],
                     'author_detail': {'name': 'Сергей Хвощевский',
                                       'href': 'https://stackoverflow.com/users/9497567'},
                     'href': 'https://stackoverflow.com/users/9497567',
                     'author': 'Сергей Хвощевский',
                     'links': [{'rel': 'alternate',
                                'href':
                                    'https://stackoverflow.com/questions/59272727/bash-exponentiation-limit',
                                'type': 'text/html'}],
                     'published': '2019-12-10T17:39:29Z',
                     'updated': '2019-12-10T18:03:14Z',
                     'summary': '<p>I want to understand the reason maximum value for '
                                '<code>$[a**b]</code> operation in Bash.</p>\n\n<pre><code>$ '
                                'echo $[2**62]\n4611686018427387904\n$ echo $['
                                '2**63]\n-9223372036854775808\n$ echo $['
                                '2**64]\n0\n</code></pre>',
                     'summary_detail': {'type': 'text/html', 'language': None,
                                        'base': 'https://stackoverflow.com/feeds/',
                                        'value': '<p>I want to understand the reason maximum '
                                                 'value for <code>$[a**b]</code> operation in '
                                                 'Bash.</p>\n\n<pre><code>$ echo $['
                                                 '2**62]\n4611686018427387904\n$ echo $['
                                                 '2**63]\n-9223372036854775808\n$ echo $['
                                                 '2**64]\n0\n</code></pre>'}},
                    {'id': 'https://stackoverflow.com/q/59272699', 'guidislink': True,
                     'link':
                         'https://stackoverflow.com/questions/59272699/django-problems-setting-up'
                         '-django-allauth-urls',
                     're_rank': {'scheme': 'https://stackoverflow.com'},
                     'title': 'Django: Problems setting up django-allauth URLs',
                     'title_detail': {'type': 'text/plain', 'language': None,
                                      'base': 'https://stackoverflow.com/feeds/',
                                      'value': 'Django: Problems setting up django-allauth '
                                               'URLs'},
                     'tags': [{'term': 'python', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None},
                              {'term': 'django', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None}, {'term': 'django-allauth',
                                                'scheme': 'https://stackoverflow.com/tags',
                                                'label': None}], 'authors': [
                        {'name': 'Elias Suess',
                         'href': 'https://stackoverflow.com/users/6361134'}],
                     'author_detail': {'name': 'Elias Suess',
                                       'href': 'https://stackoverflow.com/users/6361134'},
                     'href': 'https://stackoverflow.com/users/6361134', 'author': 'Elias Suess',
                     'links': [{'rel': 'alternate',
                                'href':
                                    'https://stackoverflow.com/questions/59272699/django-problems-setting-up-django'
                                    '-allauth-urls',
                                'type': 'text/html'}], 'published': '2019-12-10T17:37:40Z',
                     'updated': '2019-12-10T18:03:12Z',
                     'summary': '<p>I\'m trying to customize a few things of allauth and ran '
                                'into the following problem. I got my own account app, '
                                'which is supposed to handle all the customization I do to '
                                'allauth amongst other account related stuff.  '
                                '</p>\n\n<p>Which means I want to include the allauth urls '
                                'into the urls.py located in my account app, not in the '
                                'project level urls.py. However when I try it with the code '
                                'below I run into the following '
                                'error:</p>\n\n<p><code>django.urls.exceptions.NoReverseMatch: '
                                'Reverse for \'account_login\' not found. \'account_login\' is not a '
                                'valid view function or pattern '
                                'name.</code></p>\n\n<p><strong>project/urls.py</strong></p>\n\n<pre><code'
                                '>urlpatterns = [\n    path(\'admin/\', admin.site.urls),\n]\n\nurlpatterns += '
                                'i18n_patterns(\n    ...\n    path(\'account/\', include(\'apps.account.urls\')),    '
                                '# This does not work\n    # path(\'account/\', include(\'allauth.urls\')),       '
                                '# This works\n   '
                                '...\n)\n</code></pre>\n\n<p><strong>apps/account/urls.py</strong></p>\n\n<pre><code'
                                '>urlpatterns = [\n    ...\n    path(\'\', include(\'allauth.urls\')),    '
                                '#This is where I want to include the allauth urls\n    '
                                '...\n)\n</code></pre>\n\n<p>Going one step further: Can I customize the allauth '
                                'urls in some way? When I try something like the following I get the same error as '
                                'above:</p>\n\n<p><strong>apps/account/urls.py</strong></p>\n\n<pre><code>from '
                                'allauth.account import views as allauth_view\n\n\nurlpatterns = [\n    ...\n    '
                                'path("login_custom/", allauth_view.login, name="account_login"),'
                                '\n    ...\n)\n</code></pre>\n\n<p>EDIT: The last part with the custom url for '
                                'logins actually works, but only if I include all of the allauth urls in my project '
                                'level urls.py as well.</p>',
                     'summary_detail': {'type': 'text/html', 'language': None,
                                        'base': 'https://stackoverflow.com/feeds/',
                                        'value': '<p>I\'m trying to customize a few things of '
                                                 'allauth and ran into the following problem. '
                                                 'I got my own account app, which is supposed '
                                                 'to handle all the customization I do to '
                                                 'allauth amongst other account related '
                                                 'stuff.  </p>\n\n<p>Which means I want to '
                                                 'include the allauth urls into the urls.py '
                                                 'located in my account app, not in the '
                                                 'project level urls.py. However when I try '
                                                 'it with the code below I run into the '
                                                 'following '
                                                 'error:</p>\n\n<p><code>django.urls.exceptions.NoReverseMatch: '
                                                 'Reverse for \'account_login\' not found. \'account_login\' is not '
                                                 'a valid view function or pattern '
                                                 'name.</code></p>\n\n<p><strong>project/urls.py</strong></p>\n\n<pre>'
                                                 '<code>urlpatterns = [\n    path(\'admin/\', admin.site.urls),'
                                                 '\n]\n\nurlpatterns += i18n_patterns(\n    ...\n    path('
                                                 '\'account/\', include(\'apps.account.urls\')),    # This does not '
                                                 'work\n    # path(\'account/\', include(\'allauth.urls\')),       '
                                                 '# This works\n   '
                                                 '...\n)\n</code></pre>\n\n<p><strong>apps/account/urls.py</strong></p>'
                                                 '\n\n<pre><code>urlpatterns = [\n    ...\n    path(\'\', '
                                                 'include(\'allauth.urls\')),    #This is where I want to include '
                                                 'the allauth urls\n    ...\n)\n</code></pre>\n\n<p>Going one step '
                                                 'further: Can I customize the allauth urls in some way? When I try '
                                                 'something like the following I get the same error as '
                                                 'above:</p>\n\n<p><strong>apps/account/urls.py</strong></p>\n\n<pre>'
                                                 '<code>from allauth.account import views as '
                                                 'allauth_view\n\n\nurlpatterns = [\n    ...\n    path('
                                                 '"login_custom/", allauth_view.login, name="account_login"),'
                                                 '\n    ...\n)\n</code></pre>\n\n<p>EDIT: The last part with the '
                                                 'custom url for logins actually works, but only if I include all of '
                                                 'the allauth urls in my project level urls.py as well.</p>'}},
                    {'id': 'https://stackoverflow.com/q/59272653', 'guidislink': True,
                     'link':
                         'https://stackoverflow.com/questions/59272653/how-can-i-assign-a-keyboard'
                         '-stroke-to-a-button',
                     're_rank': {'scheme': 'https://stackoverflow.com'},
                     'title': 'How can i assign a Keyboard stroke to a button?',
                     'title_detail': {'type': 'text/plain', 'language': None,
                                      'base': 'https://stackoverflow.com/feeds/',
                                      'value': 'How can i assign a Keyboard stroke to a '
                                               'button?'},
                     'tags': [{'term': 'javascript', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None},
                              {'term': 'html', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None}], 'authors': [
                        {'name': 'Chris', 'href': 'https://stackoverflow.com/users/12282329'}],
                     'author_detail': {'name': 'Chris',
                                       'href': 'https://stackoverflow.com/users/12282329'},
                     'href': 'https://stackoverflow.com/users/12282329', 'author': 'Chris',
                     'links': [{'rel': 'alternate',
                                'href':
                                    'https://stackoverflow.com/questions/59272653/how-can-i-assign-a-keyboard-stroke'
                                    '-to-a-button',
                                'type': 'text/html'}], 'published': '2019-12-10T17:34:04Z',
                     'updated': '2019-12-10T18:04:01Z',
                     'summary': '<p>I have a text adventure game where the user needs to '
                                'enter commands to proceed through the game. so instead of '
                                'them having to click on the GO! button, I want them to just '
                                'be able to press enter.</p>\n\n<p>How do I assign the Enter '
                                'key, to that button.</p>',
                     'summary_detail': {'type': 'text/html', 'language': None,
                                        'base': 'https://stackoverflow.com/feeds/',
                                        'value': '<p>I have a text adventure game where the '
                                                 'user needs to enter commands to proceed '
                                                 'through the game. so instead of them having '
                                                 'to click on the GO! button, I want them to '
                                                 'just be able to press enter.</p>\n\n<p>How '
                                                 'do I assign the Enter key, '
                                                 'to that button.</p>'}},
                    {'id': 'https://stackoverflow.com/q/59272423', 'guidislink': True,
                     'link':
                         'https://stackoverflow.com/questions/59272423/how-to-get-the-return-value-of'
                         '-an-event-handler',
                     're_rank': {'scheme': 'https://stackoverflow.com'},
                     'title': 'How to get the return value of an event handler?',
                     'title_detail': {'type': 'text/plain', 'language': None,
                                      'base': 'https://stackoverflow.com/feeds/',
                                      'value': 'How to get the return value of an event '
                                               'handler?'},
                     'tags': [{'term': 'javascript', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None},
                              {'term': 'callback', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None},
                              {'term': 'dom-events', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None}], 'authors': [{'name': 'PanKitek',
                                                             'href':
                                                                 'https://stackoverflow.com/users/10930477'}],
                     'author_detail': {'name': 'PanKitek',
                                       'href': 'https://stackoverflow.com/users/10930477'},
                     'href': 'https://stackoverflow.com/users/10930477', 'author': 'PanKitek',
                     'links': [{'rel': 'alternate',
                                'href':
                                    'https://stackoverflow.com/questions/59272423/how-to-get-the-return-value-of-an'
                                    '-event-handler',
                                'type': 'text/html'}], 'published': '2019-12-10T17:16:48Z',
                     'updated': '2019-12-10T18:03:30Z',
                     'summary': '<p>I would like to return from the function of an event some '
                                'value.</p>\n\n<p>Below, you can find html and js where I\'ve '
                                'put a button. I would like to have an output true or false. '
                                'I have only information about event type in the console but '
                                'I do not know how to put true or false value outside the '
                                'function to a variable (or to another function - I would '
                                'like to make of this information as a parameter in a '
                                'different place).</p>\n\n<pre><code>    &lt;body '
                                'class="container"&gt;\n     &lt;button '
                                'class="button"&gt;Click me&lt;/button&gt;\n\n     &lt;script '
                                'src="app.js"&gt;&lt;/script&gt;\n    '
                                '&lt;/body&gt;\n</code></pre>\n\n<pre><code>    '
                                'document.addEventListener("DOMContentLoaded", function() {\n '
                                '       function clickFunct(e){\n            if('
                                'e.target.classList.contains("button")){\n                '
                                'console.log(e.type);\n                return true\n          '
                                '  }\n            else{\n                console.log("to nie '
                                'przycisk")\n                return false\n            }\n    '
                                '    }\n        document.addEventListener("click", '
                                'clickFunct);\n        })\n    });\n</code></pre>\n\n<p>I\'ve '
                                'removed "my tries" from code to have transparent code.</p>',
                     'summary_detail': {'type': 'text/html', 'language': None,
                                        'base': 'https://stackoverflow.com/feeds/',
                                        'value': '<p>I would like to return from the function '
                                                 'of an event some value.</p>\n\n<p>Below, '
                                                 'you can find html and js where I\'ve put a '
                                                 'button. I would like to have an output true '
                                                 'or false. I have only information about '
                                                 'event type in the console but I do not know '
                                                 'how to put true or false value outside the '
                                                 'function to a variable (or to another '
                                                 'function - I would like to make of this '
                                                 'information as a parameter in a different '
                                                 'place).</p>\n\n<pre><code>    &lt;body '
                                                 'class="container"&gt;\n     &lt;button '
                                                 'class="button"&gt;Click '
                                                 'me&lt;/button&gt;\n\n     &lt;script '
                                                 'src="app.js"&gt;&lt;/script&gt;\n    '
                                                 '&lt;/body&gt;\n</code></pre>\n\n<pre><code> '
                                                 '   document.addEventListener('
                                                 '"DOMContentLoaded", function() {\n        '
                                                 'function clickFunct(e){\n            if('
                                                 'e.target.classList.contains("button")){\n   '
                                                 '             console.log(e.type);\n         '
                                                 '       return true\n            }\n         '
                                                 '   else{\n                console.log("to '
                                                 'nie przycisk")\n                return '
                                                 'false\n            }\n        }\n        '
                                                 'document.addEventListener("click", '
                                                 'clickFunct);\n        })\n    '
                                                 '});\n</code></pre>\n\n<p>I\'ve removed "my '
                                                 'tries" from code to have transparent '
                                                 'code.</p>'}},
                    {'id': 'https://stackoverflow.com/q/59272029', 'guidislink': True,
                     'link':
                         'https://stackoverflow.com/questions/59272029/error-when-trying-to-write-in'
                         '-the-turtle-window',
                     're_rank': {'scheme': 'https://stackoverflow.com'},
                     'title': 'error when trying to write in the turtle window',
                     'title_detail': {'type': 'text/plain', 'language': None,
                                      'base': 'https://stackoverflow.com/feeds/',
                                      'value': 'error when trying to write in the turtle '
                                               'window'},
                     'tags': [{'term': 'python', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None}], 'authors': [{'name': 'Augustin Coman',
                                                             'href':
                                                                 'https://stackoverflow.com/users/11955911'}],
                     'author_detail': {'name': 'Augustin Coman',
                                       'href': 'https://stackoverflow.com/users/11955911'},
                     'href': 'https://stackoverflow.com/users/11955911',
                     'author': 'Augustin Coman',
                     'links': [{'rel': 'alternate',
                                'href':
                                    'https://stackoverflow.com/questions/59272029/error-when-trying-to-write-in-the'
                                    '-turtle-window',
                                'type': 'text/html'}],
                     'published': '2019-12-10T16:50:45Z',
                     'updated': '2019-12-10T18:03:44Z',
                     'summary': '<p>I get this error:</p>\n\n<pre><code> Traceback (most '
                                'recent call last):\nFile "c:\\_Muh '
                                'Stuff\\IT\\Learning\\Python\\Projet Hanoi\\Main_Program.py", '
                                'line 106, in &lt;module&gt;\n    tab_res()\n  File "c:\\_Muh '
                                'Stuff\\IT\\Learning\\Python\\Projet Hanoi\\Partie_E.py", '
                                'line 81, in tab_res\n    write(elem, ": ", all_keys[i], '
                                '"\\n")\n  File "&lt;string&gt;", line 8, in write\n  File '
                                '"C:\\Users\\Augustin\\AppData\\Local\\Programs\\Python\\Python37-32\\lib\\turtle.py'
                                '", line 3431, in write\n    end = self._write(str(arg), align.lower(), '
                                'font)\nAttributeError: \'int\' object has no attribute '
                                '\'lower\'\n</code></pre>\n\n<p>From this code:</p>\n\n<pre><code>`for i in range(0, '
                                'len(all_keys)):\n    if i == 6:\n        break\n\n    elem = dict1[all_keys[i]]\n\n '
                                '   print(elem, ": ", all_keys[i])\n\n    turtle.write(elem, ": ", all_keys[i], '
                                '"\\n")\n\n    del dict1[all_keys[i]]`\n</code></pre>\n\n<p>I just don\'t understand '
                                'how this error is linked to turtle</p>\n\n<p>Could it be because of the "\\n" at '
                                'the end??</p>',
                     'summary_detail': {'type': 'text/html', 'language': None,
                                        'base': 'https://stackoverflow.com/feeds/',
                                        'value': '<p>I get this error:</p>\n\n<pre><code> '
                                                 'Traceback (most recent call last):\nFile '
                                                 '"c:\\_Muh '
                                                 'Stuff\\IT\\Learning\\Python\\Projet '
                                                 'Hanoi\\Main_Program.py", line 106, '
                                                 'in &lt;module&gt;\n    tab_res()\n  File '
                                                 '"c:\\_Muh '
                                                 'Stuff\\IT\\Learning\\Python\\Projet '
                                                 'Hanoi\\Partie_E.py", line 81, in tab_res\n  '
                                                 '  write(elem, ": ", all_keys[i], '
                                                 '"\\n")\n  File "&lt;string&gt;", line 8, '
                                                 'in write\n  File '
                                                 '"C:\\Users\\Augustin\\AppData\\Local\\Programs\\Python\\Python37-32'
                                                 '\\lib\\turtle.py", line 3431, in write\n    end = self._write(str('
                                                 'arg), align.lower(), font)\nAttributeError: \'int\' object has no '
                                                 'attribute \'lower\'\n</code></pre>\n\n<p>From this '
                                                 'code:</p>\n\n<pre><code>`for i in range(0, len(all_keys)):\n    if '
                                                 'i == 6:\n        break\n\n    elem = dict1[all_keys[i]]\n\n    '
                                                 'print(elem, ": ", all_keys[i])\n\n    turtle.write(elem, ": ", '
                                                 'all_keys[i], "\\n")\n\n    del dict1[all_keys['
                                                 'i]]`\n</code></pre>\n\n<p>I just don\'t understand how this error '
                                                 'is linked to turtle</p>\n\n<p>Could it be because of the "\\n" at '
                                                 'the end??</p>'}},
                    {'id': 'https://stackoverflow.com/q/59271856', 'guidislink': True,
                     'link':
                         'https://stackoverflow.com/questions/59271856/regematch-if-and-and-date'
                         '-combined-forumula',
                     're_rank': {'scheme': 'https://stackoverflow.com'},
                     'title': 'Regematch if, and, and date combined forumula',
                     'title_detail': {'type': 'text/plain', 'language': None,
                                      'base': 'https://stackoverflow.com/feeds/',
                                      'value': 'Regematch if, and, and date combined forumula'},
                     'tags': [{'term': 'regex', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None}, {'term': 'if-statement',
                                                'scheme': 'https://stackoverflow.com/tags',
                                                'label': None}, {'term': 'google-sheets',
                                                                 'scheme':
                                                                     'https://stackoverflow.com/tags',
                                                                 'label': None},
                              {'term': 'google-sheets-formula',
                               'scheme': 'https://stackoverflow.com/tags', 'label': None},
                              {'term': 'array-formulas',
                               'scheme': 'https://stackoverflow.com/tags', 'label': None}],
                     'authors': [{'name': 'BrettG',
                                  'href': 'https://stackoverflow.com/users/12512775'}],
                     'author_detail': {'name': 'BrettG',
                                       'href': 'https://stackoverflow.com/users/12512775'},
                     'href': 'https://stackoverflow.com/users/12512775', 'author': 'BrettG',
                     'links': [{'rel': 'alternate',
                                'href':
                                    'https://stackoverflow.com/questions/59271856/regematch-if-and-and-date-combined'
                                    '-forumula',
                                'type': 'text/html'}], 'published': '2019-12-10T16:39:38Z',
                     'updated': '2019-12-10T18:03:08Z',
                     'summary': '<p>I need help trying to figure out a combination google '
                                'sheets formula</p>\n\n<pre><code>If \n    Cell B5 contains '
                                '"Rct"\nAnd\n    today\'s date is 30 days after the date '
                                'defined in cell C5\nAnd\n    if Cell D5 and D6 both says "2 '
                                'weeks ago" or "1 week ago" or contains the words "day" '
                                '"hour" or "minute"\n</code></pre>\n\n<p>(not sure if '
                                'possible but instead of the all those words could if be if '
                                'the text in cell D5 and D6 are the color "green" and or '
                                '"Yellow")</p>\n\n<pre><code>Then\n    Cell H5 will say "Y" '
                                'if the above conditions are met or "N" if they '
                                'aren\'t\n</code></pre>\n\n<p>The following formula works for '
                                'what I asked above</p>\n\n<pre><code>=ARRAYFORMULA(IF(('
                                'REGEXMATCH(LOWER(B5:B29), "rct"))*\n             (TODAY('
                                ')&gt;C5:C29+30)*\n             (REGEXMATCH(LOWER(D5:D29), '
                                '"2 weeks ago|1 week ago|day|hour|minute"))*\n             ('
                                'REGEXMATCH(LOWER(E5:E29), "2 weeks ago|1 week '
                                'ago|day|hour|minute")), \n             "Y", '
                                '"N"))\n</code></pre>\n\n<p>However I am new to doing this '
                                'coding stuff on the google sheets and I though I could add '
                                'to that formula myself without troubling someone '
                                'else.</p>\n\n<p>Is there any way to add to that formula so '
                                'that</p>\n\n<pre><code>If\n    Cell B5:B28 contains '
                                '"cdt"\nand\n    today\'s date is 60 days after the date '
                                'defined in cell F5:F29\nAnd\n   if Cell D5 and D6 both says '
                                '"2 weeks ago" or "1 week ago" or contains the words "day" '
                                '"hour" or "minute"\nThen\n    Cell H5 will say "Y" if the '
                                'above conditions are met or "N" if they '
                                'aren\'t\n</code></pre>\n\n<p>as well '
                                'as</p>\n\n<pre><code>If\n   Cell B5:B28 contains '
                                '"pvt"\nand\n   today\'s date is 90 days after the date '
                                'defined in cell F5:F29\nAnd\n   if Cell D5 and D6 both says '
                                '"2 weeks ago" or "1 week ago" or contains the words "day" '
                                '"hour" or "minute"\nThen\n    Cell H5 will say "Y" if the '
                                'above conditions are met or "N" if they '
                                'aren\'t\n</code></pre>\n\n<p><img alt="Picture of my google '
                                'sheet" src="https://i.stack.imgur.com/SGoDV.png" /></p>',
                     'summary_detail': {'type': 'text/html', 'language': None,
                                        'base': 'https://stackoverflow.com/feeds/',
                                        'value': '<p>I need help trying to figure out a '
                                                 'combination google sheets '
                                                 'formula</p>\n\n<pre><code>If \n    Cell B5 '
                                                 'contains "Rct"\nAnd\n    today\'s date is '
                                                 '30 days after the date defined in cell '
                                                 'C5\nAnd\n    if Cell D5 and D6 both says "2 '
                                                 'weeks ago" or "1 week ago" or contains the '
                                                 'words "day" "hour" or '
                                                 '"minute"\n</code></pre>\n\n<p>(not sure if '
                                                 'possible but instead of the all those words '
                                                 'could if be if the text in cell D5 and D6 '
                                                 'are the color "green" and or '
                                                 '"Yellow")</p>\n\n<pre><code>Then\n    Cell '
                                                 'H5 will say "Y" if the above conditions are '
                                                 'met or "N" if they '
                                                 'aren\'t\n</code></pre>\n\n<p>The following '
                                                 'formula works for what I asked '
                                                 'above</p>\n\n<pre><code>=ARRAYFORMULA(IF(('
                                                 'REGEXMATCH(LOWER(B5:B29), "rct"))*\n        '
                                                 '     (TODAY()&gt;C5:C29+30)*\n             '
                                                 '(REGEXMATCH(LOWER(D5:D29), "2 weeks ago|1 '
                                                 'week ago|day|hour|minute"))*\n             '
                                                 '(REGEXMATCH(LOWER(E5:E29), "2 weeks ago|1 '
                                                 'week ago|day|hour|minute")), \n             '
                                                 '"Y", "N"))\n</code></pre>\n\n<p>However I '
                                                 'am new to doing this coding stuff on the '
                                                 'google sheets and I though I could add to '
                                                 'that formula myself without troubling '
                                                 'someone else.</p>\n\n<p>Is there any way to '
                                                 'add to that formula so '
                                                 'that</p>\n\n<pre><code>If\n    Cell B5:B28 '
                                                 'contains "cdt"\nand\n    today\'s date is '
                                                 '60 days after the date defined in cell '
                                                 'F5:F29\nAnd\n   if Cell D5 and D6 both says '
                                                 '"2 weeks ago" or "1 week ago" or contains '
                                                 'the words "day" "hour" or "minute"\nThen\n  '
                                                 '  Cell H5 will say "Y" if the above '
                                                 'conditions are met or "N" if they '
                                                 'aren\'t\n</code></pre>\n\n<p>as well '
                                                 'as</p>\n\n<pre><code>If\n   Cell B5:B28 '
                                                 'contains "pvt"\nand\n   today\'s date is 90 '
                                                 'days after the date defined in cell '
                                                 'F5:F29\nAnd\n   if Cell D5 and D6 both says '
                                                 '"2 weeks ago" or "1 week ago" or contains '
                                                 'the words "day" "hour" or "minute"\nThen\n  '
                                                 '  Cell H5 will say "Y" if the above '
                                                 'conditions are met or "N" if they '
                                                 'aren\'t\n</code></pre>\n\n<p><img '
                                                 'alt="Picture of my google sheet" '
                                                 'src="https://i.stack.imgur.com/SGoDV.png" '
                                                 '/></p>'}},
                    {'id': 'https://stackoverflow.com/q/59271440', 'guidislink': True,
                     'link':
                         'https://stackoverflow.com/questions/59271440/grails-command-object'
                         '-validation-for-input-list',
                     're_rank': {'scheme': 'https://stackoverflow.com'},
                     'title': 'Grails Command Object validation for input list',
                     'title_detail': {'type': 'text/plain', 'language': None,
                                      'base': 'https://stackoverflow.com/feeds/',
                                      'value': 'Grails Command Object validation for input '
                                               'list'},
                     'tags': [{'term': 'grails', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None},
                              {'term': 'gorm', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None}, {'term': 'command-objects',
                                                'scheme': 'https://stackoverflow.com/tags',
                                                'label': None}], 'authors': [
                        {'name': 'Derrick', 'href': 'https://stackoverflow.com/users/4034406'}],
                     'author_detail': {'name': 'Derrick',
                                       'href': 'https://stackoverflow.com/users/4034406'},
                     'href': 'https://stackoverflow.com/users/4034406', 'author': 'Derrick',
                     'links': [{'rel': 'alternate',
                                'href':
                                    'https://stackoverflow.com/questions/59271440/grails-command-object-validation'
                                    '-for-input-list',
                                'type': 'text/html'}], 'published': '2019-12-10T16:15:40Z',
                     'updated': '2019-12-10T18:02:49Z',
                     'summary': '<p>Hi how do I set the command object constraint nullable, '
                                'blank, and custom for these 2 list, event[] and qty[] from '
                                'the below html?</p>\n\n<pre><code>&lt;div '
                                'class="row-1"&gt;\n    &lt;select name="event[]" '
                                'class="form-control "&gt;\n        &lt;option '
                                'selected=""&gt;abc&lt;/option&gt;\n        &lt;option '
                                'selected=""&gt;def&lt;/option&gt;\n    &lt;/select&gt;\n    '
                                '&lt;input name="qty[]" &gt;\n&lt;/div&gt;\n&lt;div '
                                'class="row-2"&gt;\n    &lt;select name="event[]" '
                                'class="form-control "&gt;\n        &lt;option '
                                'selected=""&gt;ghi&lt;/option&gt;\n        &lt;option '
                                'selected=""&gt;jkl&lt;/option&gt;\n    &lt;/select&gt;\n    '
                                '&lt;input name="qty[]" &gt;\n&lt;/div&gt;\n\n\nclass '
                                'someCommand implements Validateable {\n\n    List '
                                'eventComponent\n    List qty\n\n    static constraints = {\n '
                                '   }\n}\n</code></pre>',
                     'summary_detail': {'type': 'text/html', 'language': None,
                                        'base': 'https://stackoverflow.com/feeds/',
                                        'value': '<p>Hi how do I set the command object '
                                                 'constraint nullable, blank, and custom for '
                                                 'these 2 list, event[] and qty[] from the '
                                                 'below html?</p>\n\n<pre><code>&lt;div '
                                                 'class="row-1"&gt;\n    &lt;select '
                                                 'name="event[]" class="form-control "&gt;\n  '
                                                 '      &lt;option '
                                                 'selected=""&gt;abc&lt;/option&gt;\n        '
                                                 '&lt;option '
                                                 'selected=""&gt;def&lt;/option&gt;\n    '
                                                 '&lt;/select&gt;\n    &lt;input name="qty[]" '
                                                 '&gt;\n&lt;/div&gt;\n&lt;div '
                                                 'class="row-2"&gt;\n    &lt;select '
                                                 'name="event[]" class="form-control "&gt;\n  '
                                                 '      &lt;option '
                                                 'selected=""&gt;ghi&lt;/option&gt;\n        '
                                                 '&lt;option '
                                                 'selected=""&gt;jkl&lt;/option&gt;\n    '
                                                 '&lt;/select&gt;\n    &lt;input name="qty[]" '
                                                 '&gt;\n&lt;/div&gt;\n\n\nclass someCommand '
                                                 'implements Validateable {\n\n    List '
                                                 'eventComponent\n    List qty\n\n    static '
                                                 'constraints = {\n    }\n}\n</code></pre>'}},
                    {'id': 'https://stackoverflow.com/q/59271146', 'guidislink': True,
                     'link':
                         'https://stackoverflow.com/questions/59271146/django-settings-py-secret-key'
                         '-keyerror',
                     're_rank': {'scheme': 'https://stackoverflow.com'},
                     'title': 'Django Settings.py - SECRET_KEY - KeyError',
                     'title_detail': {'type': 'text/plain', 'language': None,
                                      'base': 'https://stackoverflow.com/feeds/',
                                      'value': 'Django Settings.py - SECRET_KEY - KeyError'},
                     'tags': [{'term': 'python', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None},
                              {'term': 'django', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None},
                              {'term': 'gunicorn', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None}], 'authors': [{'name': 'Boilmashstew',
                                                             'href':
                                                                 'https://stackoverflow.com/users/9816773'}],
                     'author_detail': {'name': 'Boilmashstew',
                                       'href': 'https://stackoverflow.com/users/9816773'},
                     'href': 'https://stackoverflow.com/users/9816773',
                     'author': 'Boilmashstew',
                     'links': [{'rel': 'alternate',
                                'href':
                                    'https://stackoverflow.com/questions/59271146/django-settings-py-secret-key'
                                    '-keyerror',
                                'type': 'text/html'}],
                     'published': '2019-12-10T16:00:09Z',
                     'updated': '2019-12-10T18:03:25Z',
                     'summary': '<p>Currently have a <em>Django</em> project running on '
                                'Python 3.6.9, hosted on <em>Digital ocean</em> using '
                                '<em>Gunicorn</em> and <em>Nginx</em>. </p>\n\n<p>I am '
                                'attempting to switch my <code>SECRET_KEY</code> and other '
                                'passwords to <strong>environment variables</strong> opposed '
                                'to having them as a string in <code>settings.py</code>. '
                                '</p>\n\n<p>When doing so I run into the following error and '
                                'Gunicorn shuts down.</p>\n\n<pre><code>Dec 10 15:22:20:   '
                                'File "/home/user/projectdir/project/project/settings.py", '
                                'line 23, in &lt;module&gt;\nDec 10 15:22:20 droplet_name '
                                'gunicorn:     SECRET_KEY = os.environ[\'SECRET_KEY\']\nDec '
                                '10 15:22:20 droplet_name gunicorn:   File '
                                '"/home/user/projectdir/myenv/lib/python3.6/os.py", line 669, '
                                'in __getitem__\nDec 10 15:22:20 droplet_name gunicorn:     '
                                'raise KeyError(key) from None\nDec 10 15:22:20 droplet_name '
                                'gunicorn: KeyError: \'SECRET_KEY\'\nDec 10 15:22:20 '
                                'droplet_name gunicorn: [2019-12-10 15:22:20 +0000] [20022] ['
                                'INFO] Worker exiting (pid: 20022)\n</code></pre>\n\n<p>I '
                                'have exported the <code>SECRET_KEY</code> correctly prior by '
                                'doing </p>\n\n<p><code>export '
                                'SECRET_KEY=\'my_key\'</code></p>\n\n<p>This is what my '
                                '<code>settings.py</code> looks like as '
                                'well:</p>\n\n<pre><code>import os\n\nBASE_DIR = '
                                'os.path.dirname(os.path.dirname(os.path.abspath('
                                '__file__)))\n\nSECRET_KEY = os.environ['
                                '\'SECRET_KEY\']\n\nDEBUG = False\n\nALLOWED_HOSTS = ['
                                '"my_ip"]\n\nINSTALLED_APPS = [\n    '
                                '\'django.contrib.admin\',\n    \'django.contrib.auth\','
                                '\n    \'django.contrib.contenttypes\','
                                '\n    \'django.contrib.sessions\','
                                '\n    \'django.contrib.messages\','
                                '\n    \'django.contrib.staticfiles\',\n    \'home\','
                                '\n]\n\nMIDDLEWARE = [\n    '
                                '\'django.middleware.security.SecurityMiddleware\','
                                '\n    '
                                '\'django.contrib.sessions.middleware.SessionMiddleware\','
                                '\n    \'django.middleware.common.CommonMiddleware\','
                                '\n    \'django.middleware.csrf.CsrfViewMiddleware\','
                                '\n    '
                                '\'django.contrib.auth.middleware.AuthenticationMiddleware\','
                                '\n    '
                                '\'django.contrib.messages.middleware.MessageMiddleware\','
                                '\n    '
                                '\'django.middleware.clickjacking.XFrameOptionsMiddleware\','
                                '\n]\n\nROOT_URLCONF = \'project_name.urls\'\n\nTEMPLATES = ['
                                '\n    {\n        \'BACKEND\': '
                                '\'django.template.backends.django.DjangoTemplates\','
                                '\n        \'DIRS\': [],\n        \'APP_DIRS\': True,'
                                '\n        \'OPTIONS\': {\n            '
                                '\'context_processors\': [\n                '
                                '\'django.template.context_processors.debug\',\n              '
                                '  \'django.template.context_processors.request\',\n          '
                                '      \'django.contrib.auth.context_processors.auth\','
                                '\n                '
                                '\'django.contrib.messages.context_processors.messages\','
                                '\n            ],\n        },\n    },\n]\n\nWSGI_APPLICATION '
                                '= \'project_name.wsgi.application\'\n\nDATABASES = {\n    '
                                '\'default\': {\n        \'ENGINE\': '
                                '\'django.db.backends.postgresql_psycopg2\',\n        '
                                '\'NAME\': \'projectnamedb\',\n        \'USER\': \'myuser\','
                                '\n        \'PASSWORD\': \'mypass\',\n        \'HOST\': '
                                '\'localhost\',\n        \'PORT\': \'\','
                                '\n    }\n}\n\nAUTH_PASSWORD_VALIDATORS = [\n    {\n        '
                                '\'NAME\': '
                                '\'django.contrib.auth.password_validation.UserAttributeSimilarityValidator\','
                                '\n    },\n    {\n        \'NAME\': '
                                '\'django.contrib.auth.password_validation.MinimumLengthValidator\',\n    },'
                                '\n    {\n        \'NAME\': '
                                '\'django.contrib.auth.password_validation.CommonPasswordValidator\',\n    },'
                                '\n    {\n        \'NAME\': '
                                '\'django.contrib.auth.password_validation.NumericPasswordValidator\',\n    },'
                                '\n]\n\n\nLANGUAGE_CODE = \'en-us\'\n\nTIME_ZONE = \'UTC\'\n\nUSE_I18N = '
                                'True\n\nUSE_L10N = True\n\nUSE_TZ = True\n\nSTATIC_URL = \'/static/\'\nSTATIC_ROOT '
                                '= os.path.join(BASE_DIR, \'static\')\n\nMEDIA_URL = "/media/"\nMEDIA_ROOT = '
                                'os.path.join(BASE_DIR, \'media\')\n\nLOGIN_URL = '
                                '\'/home/user_login\'\n</code></pre>\n\n<p>I have read through at least a dozen '
                                'similar posts and still cannot correct the issue. I would like to use '
                                '<code>os.environ</code> if possible without loading a new '
                                '<em>library</em>.</p>\n\n<p>UPDATE: I have placed a <code>test_one.py</code> '
                                'document in the same directory as settings.py with the following code. When ran, '
                                'it outputs the <code>SECRET_KEY</code> and returns a string as the type as '
                                'expected. Still cannot achieve the same result on the <code>settings.py</code> '
                                'file.</p>\n\n<pre><code>import os\n\nprint(os.environ[\'SECRET_KEY\'])\nprint(type('
                                'os.environ[\'SECRET_KEY\']))\n\nSECRET_KEY = os.environ[\'SECRET_KEY\']\nprint('
                                'type(SECRET_KEY))\n</code></pre>',
                     'summary_detail': {'type': 'text/html', 'language': None,
                                        'base': 'https://stackoverflow.com/feeds/',
                                        'value': '<p>Currently have a <em>Django</em> project '
                                                 'running on Python 3.6.9, hosted on '
                                                 '<em>Digital ocean</em> using '
                                                 '<em>Gunicorn</em> and <em>Nginx</em>. '
                                                 '</p>\n\n<p>I am attempting to switch my '
                                                 '<code>SECRET_KEY</code> and other passwords '
                                                 'to <strong>environment variables</strong> '
                                                 'opposed to having them as a string in '
                                                 '<code>settings.py</code>. </p>\n\n<p>When '
                                                 'doing so I run into the following error and '
                                                 'Gunicorn shuts down.</p>\n\n<pre><code>Dec '
                                                 '10 15:22:20:   File '
                                                 '"/home/user/projectdir/project/project/settings.py", line 23, '
                                                 'in &lt;module&gt;\nDec 10 15:22:20 droplet_name gunicorn:     '
                                                 'SECRET_KEY = os.environ[\'SECRET_KEY\']\nDec 10 15:22:20 '
                                                 'droplet_name gunicorn:   File '
                                                 '"/home/user/projectdir/myenv/lib/python3.6/os.py", line 669, '
                                                 'in __getitem__\nDec 10 15:22:20 droplet_name gunicorn:     raise '
                                                 'KeyError(key) from None\nDec 10 15:22:20 droplet_name gunicorn: '
                                                 'KeyError: \'SECRET_KEY\'\nDec 10 15:22:20 droplet_name gunicorn: ['
                                                 '2019-12-10 15:22:20 +0000] [20022] [INFO] Worker exiting (pid: '
                                                 '20022)\n</code></pre>\n\n<p>I have exported the '
                                                 '<code>SECRET_KEY</code> correctly prior by doing '
                                                 '</p>\n\n<p><code>export '
                                                 'SECRET_KEY=\'my_key\'</code></p>\n\n<p>This is what my '
                                                 '<code>settings.py</code> looks like as '
                                                 'well:</p>\n\n<pre><code>import os\n\nBASE_DIR = os.path.dirname('
                                                 'os.path.dirname(os.path.abspath(__file__)))\n\nSECRET_KEY = '
                                                 'os.environ[\'SECRET_KEY\']\n\nDEBUG = False\n\nALLOWED_HOSTS = ['
                                                 '"my_ip"]\n\nINSTALLED_APPS = [\n    \'django.contrib.admin\','
                                                 '\n    \'django.contrib.auth\','
                                                 '\n    \'django.contrib.contenttypes\','
                                                 '\n    \'django.contrib.sessions\','
                                                 '\n    \'django.contrib.messages\','
                                                 '\n    \'django.contrib.staticfiles\',\n    \'home\','
                                                 '\n]\n\nMIDDLEWARE = [\n    '
                                                 '\'django.middleware.security.SecurityMiddleware\','
                                                 '\n    \'django.contrib.sessions.middleware.SessionMiddleware\','
                                                 '\n    \'django.middleware.common.CommonMiddleware\','
                                                 '\n    \'django.middleware.csrf.CsrfViewMiddleware\','
                                                 '\n    \'django.contrib.auth.middleware.AuthenticationMiddleware\','
                                                 '\n    \'django.contrib.messages.middleware.MessageMiddleware\','
                                                 '\n    \'django.middleware.clickjacking.XFrameOptionsMiddleware\','
                                                 '\n]\n\nROOT_URLCONF = \'project_name.urls\'\n\nTEMPLATES = [\n    '
                                                 '{\n        \'BACKEND\': '
                                                 '\'django.template.backends.django.DjangoTemplates\','
                                                 '\n        \'DIRS\': [],\n        \'APP_DIRS\': True,'
                                                 '\n        \'OPTIONS\': {\n            \'context_processors\': [\n  '
                                                 '              \'django.template.context_processors.debug\','
                                                 '\n                \'django.template.context_processors.request\','
                                                 '\n                \'django.contrib.auth.context_processors.auth\','
                                                 '\n                '
                                                 '\'django.contrib.messages.context_processors.messages\','
                                                 '\n            ],\n        },\n    },\n]\n\nWSGI_APPLICATION = '
                                                 '\'project_name.wsgi.application\'\n\nDATABASES = {\n    '
                                                 '\'default\': {\n        \'ENGINE\': '
                                                 '\'django.db.backends.postgresql_psycopg2\',\n        \'NAME\': '
                                                 '\'projectnamedb\',\n        \'USER\': \'myuser\',\n        '
                                                 '\'PASSWORD\': \'mypass\',\n        \'HOST\': \'localhost\','
                                                 '\n        \'PORT\': \'\',\n    }\n}\n\nAUTH_PASSWORD_VALIDATORS = '
                                                 '[\n    {\n        \'NAME\': '
                                                 '\'django.contrib.auth.password_validation.'
                                                 'UserAttributeSimilarityValidator\',\n    },\n    {\n        '
                                                 '\'NAME\': '
                                                 '\'django.contrib.auth.password_validation.MinimumLengthValidator\','
                                                 '\n    },\n    {\n        \'NAME\': '
                                                 '\'django.contrib.auth.password_validation.CommonPasswordValidator\','
                                                 '\n    },\n    {\n        \'NAME\': '
                                                 '\'django.contrib.auth.password_validation.NumericPasswordValidator\''
                                                 ',\n    },\n]\n\n\nLANGUAGE_CODE = \'en-us\'\n\nTIME_ZONE = '
                                                 '\'UTC\'\n\nUSE_I18N = True\n\nUSE_L10N = True\n\nUSE_TZ = '
                                                 'True\n\nSTATIC_URL = \'/static/\'\nSTATIC_ROOT = os.path.join('
                                                 'BASE_DIR, \'static\')\n\nMEDIA_URL = "/media/"\nMEDIA_ROOT = '
                                                 'os.path.join(BASE_DIR, \'media\')\n\nLOGIN_URL = '
                                                 '\'/home/user_login\'\n</code></pre>\n\n<p>I have read through at '
                                                 'least a dozen similar posts and still cannot correct the issue. I '
                                                 'would like to use <code>os.environ</code> if possible without '
                                                 'loading a new <em>library</em>.</p>\n\n<p>UPDATE: I have placed a '
                                                 '<code>test_one.py</code> document in the same directory as '
                                                 'settings.py with the following code. When ran, it outputs the '
                                                 '<code>SECRET_KEY</code> and returns a string as the type as '
                                                 'expected. Still cannot achieve the same result on the '
                                                 '<code>settings.py</code> file.</p>\n\n<pre><code>import '
                                                 'os\n\nprint(os.environ[\'SECRET_KEY\'])\nprint(type(os.environ['
                                                 '\'SECRET_KEY\']))\n\nSECRET_KEY = os.environ['
                                                 '\'SECRET_KEY\']\nprint(type(SECRET_KEY))\n</code></pre>'}},
                    {'id': 'https://stackoverflow.com/q/59270651', 'guidislink': True,
                     'link':
                         'https://stackoverflow.com/questions/59270651/mathematical-operations'
                         '-without-using-java-math-class',
                     're_rank': {'scheme': 'https://stackoverflow.com'},
                     'title': 'Mathematical Operations Without Using Java Math Class',
                     'title_detail': {'type': 'text/plain', 'language': None,
                                      'base': 'https://stackoverflow.com/feeds/',
                                      'value': 'Mathematical Operations Without Using Java '
                                               'Math Class'},
                     'tags': [{'term': 'java', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None},
                              {'term': 'math', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None}], 'authors': [{'name': 'Johnathan Davidow',
                                                             'href':
                                                                 'https://stackoverflow.com/users/12511783'}],
                     'author_detail': {'name': 'Johnathan Davidow',
                                       'href': 'https://stackoverflow.com/users/12511783'},
                     'href': 'https://stackoverflow.com/users/12511783',
                     'author': 'Johnathan Davidow',
                     'links': [{'rel': 'alternate',
                                'href':
                                    'https://stackoverflow.com/questions/59270651/mathematical-operations-without'
                                    '-using-java-math-class',
                                'type': 'text/html'}],
                     'published': '2019-12-10T15:32:25Z',
                     'updated': '2019-12-10T18:03:46Z',
                     'summary': "<p>I've been making my own class library in Java and I've "
                                "run into a small annoyance. The library is centered around "
                                "<em>math</em>. I started with the intention of not using the "
                                "<em>Java Math Class</em>. Unfortunately, my lack of skill "
                                "paired with my inability to find a resource online that "
                                "tackles this problem has resulted in me falling back onto "
                                "the Java Math Class. <strong>Is there a way I can do "
                                "logarithms without using Math.log?</strong></p>",
                     'summary_detail': {'type': 'text/html', 'language': None,
                                        'base': 'https://stackoverflow.com/feeds/',
                                        'value': "<p>I've been making my own class library in "
                                                 "Java and I've run into a small annoyance. "
                                                 "The library is centered around "
                                                 "<em>math</em>. I started with the intention "
                                                 "of not using the <em>Java Math Class</em>. "
                                                 "Unfortunately, my lack of skill paired with "
                                                 "my inability to find a resource online that "
                                                 "tackles this problem has resulted in me "
                                                 "falling back onto the Java Math Class. "
                                                 "<strong>Is there a way I can do logarithms "
                                                 "without using Math.log?</strong></p>"}},
                    {'id': 'https://stackoverflow.com/q/59268178', 'guidislink': True,
                     'link':
                         'https://stackoverflow.com/questions/59268178/dependency-issue-with-spark'
                         '-and-google-cloud-firestore-with-sbt',
                     're_rank': {'scheme': 'https://stackoverflow.com'},
                     'title': 'Dependency issue with Spark and Google cloud Firestore with SBT',
                     'title_detail': {'type': 'text/plain', 'language': None,
                                      'base': 'https://stackoverflow.com/feeds/',
                                      'value': 'Dependency issue with Spark and Google cloud '
                                               'Firestore with SBT'},
                     'tags': [{'term': 'java', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None},
                              {'term': 'scala', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None}, {'term': 'apache-spark',
                                                'scheme': 'https://stackoverflow.com/tags',
                                                'label': None},
                              {'term': 'google-cloud-platform',
                               'scheme': 'https://stackoverflow.com/tags', 'label': None},
                              {'term': 'sbt', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None}], 'authors': [
                        {'name': 'SimbaPK', 'href': 'https://stackoverflow.com/users/8935317'}],
                     'author_detail': {'name': 'SimbaPK',
                                       'href': 'https://stackoverflow.com/users/8935317'},
                     'href': 'https://stackoverflow.com/users/8935317', 'author': 'SimbaPK',
                     'links': [{'rel': 'alternate',
                                'href':
                                    'https://stackoverflow.com/questions/59268178/dependency-issue-with-spark-and'
                                    '-google-cloud-firestore-with-sbt',
                                'type': 'text/html'}], 'published': '2019-12-10T13:19:10Z',
                     'updated': '2019-12-10T18:04:07Z',
                     'summary': '<p>My project runs without issues in Intellij sbt console. '
                                '</p>\n\n<p>But after compiling with sbt assembly when I run '
                                'the jar with spark-submit, I get this: '
                                '</p>\n\n<pre><code>Exception in thread "main" '
                                'java.lang.NoSuchMethodError: '
                                'com.google.common.base.Preconditions.checkArgument('
                                'ZLjava/lang/String;CLjava/lang/Object;)V\n</code></pre>\n\n<p>I '
                                'tried a lot of different things around my dependencies, '
                                'following GCP advice <a '
                                'href="https://cloud.google.com/blog/products/data-analytics/managing-java'
                                '-dependencies-apache-spark-applications-cloud-dataproc" rel="nofollow '
                                'noreferrer">here</a></p>\n\n<p>I use sbt with assembly plugin. </p>\n\n<p>Here\'s '
                                'my sbt file : </p>\n\n<pre><code>name := "firestore-dump"\n\nversion := '
                                '"0.1"\n\nscalaVersion := "2.11.8"\n\nlibraryDependencies += "com.google.firebase" % '
                                '"firebase-admin" % "6.11.0"\n\nlibraryDependencies += "org.apache.spark" %% '
                                '"spark-sql" % "2.4.4"\n\nlibraryDependencies += "org.yaml" % "snakeyaml" % '
                                '"1.18"\nlibraryDependencies += "net.liftweb" %% "lift-json" % '
                                '"3.3.0"\n\nassemblyShadeRules in assembly := Seq(\n  ShadeRule.rename('
                                '"com.google.common.**" -&gt; "repackaged.com.google.common.@1").inAll,'
                                '\n  ShadeRule.rename("com.google.protobuf.**" -&gt; '
                                '"repackaged.com.google.protobuf.@1").inAll\n)\n\nassemblyMergeStrategy in assembly '
                                ':= {\n  entry: String =&gt; {\n    val strategy = (assemblyMergeStrategy in '
                                'assembly).value(entry)\n    if (strategy == MergeStrategy.deduplicate) '
                                'MergeStrategy.first\n    else strategy\n  }\n}\n</code></pre>\n\n<p>Any help would '
                                'be appreciated </p>',
                     'summary_detail': {'type': 'text/html', 'language': None,
                                        'base': 'https://stackoverflow.com/feeds/',
                                        'value': '<p>My project runs without issues in '
                                                 'Intellij sbt console. </p>\n\n<p>But after '
                                                 'compiling with sbt assembly when I run the '
                                                 'jar with spark-submit, I get this: '
                                                 '</p>\n\n<pre><code>Exception in thread '
                                                 '"main" java.lang.NoSuchMethodError: '
                                                 'com.google.common.base.Preconditions.checkArgument('
                                                 'ZLjava/lang/String;CLjava/lang/Object;)V\n</code></pre>\n\n<p>I '
                                                 'tried a lot of different things around my dependencies, '
                                                 'following GCP advice <a '
                                                 'href="https://cloud.google.com/blog/products/data-analytics/managing'
                                                 '-java-dependencies-apache-spark-applications-cloud-dataproc" '
                                                 'rel="nofollow noreferrer">here</a></p>\n\n<p>I use sbt with '
                                                 'assembly plugin. </p>\n\n<p>Here\'s my sbt file : '
                                                 '</p>\n\n<pre><code>name := "firestore-dump"\n\nversion := '
                                                 '"0.1"\n\nscalaVersion := "2.11.8"\n\nlibraryDependencies += '
                                                 '"com.google.firebase" % "firebase-admin" % '
                                                 '"6.11.0"\n\nlibraryDependencies += "org.apache.spark" %% '
                                                 '"spark-sql" % "2.4.4"\n\nlibraryDependencies += "org.yaml" % '
                                                 '"snakeyaml" % "1.18"\nlibraryDependencies += "net.liftweb" %% '
                                                 '"lift-json" % "3.3.0"\n\nassemblyShadeRules in assembly := Seq(\n  '
                                                 'ShadeRule.rename("com.google.common.**" -&gt; '
                                                 '"repackaged.com.google.common.@1").inAll,\n  ShadeRule.rename('
                                                 '"com.google.protobuf.**" -&gt; '
                                                 '"repackaged.com.google.protobuf.@1").inAll\n)\n\n'
                                                 'assemblyMergeStrategy in assembly := {\n  entry: String =&gt; {\n  '
                                                 '  val strategy = (assemblyMergeStrategy in assembly).value('
                                                 'entry)\n    if (strategy == MergeStrategy.deduplicate) '
                                                 'MergeStrategy.first\n    else strategy\n  '
                                                 '}\n}\n</code></pre>\n\n<p>Any help would be appreciated </p>'}},
                    {'id': 'https://stackoverflow.com/q/59266166', 'guidislink': True,
                     'link':
                         'https://stackoverflow.com/questions/59266166/do-messages-form-coinbase'
                         '-websocket-full-channel-have-a-constant-format',
                     're_rank': {'scheme': 'https://stackoverflow.com'},
                     'title': "Do messages form Coinbase websocket 'FULL' channel have a "
                              "constant format",
                     'title_detail': {'type': 'text/plain', 'language': None,
                                      'base': 'https://stackoverflow.com/feeds/',
                                      'value': "Do messages form Coinbase websocket 'FULL' "
                                               "channel have a constant format"},
                     'tags': [{'term': 'json', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None},
                              {'term': 'websocket', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None}, {'term': 'coinbase-api',
                                                'scheme': 'https://stackoverflow.com/tags',
                                                'label': None}], 'authors': [
                        {'name': 'huhnmonster',
                         'href': 'https://stackoverflow.com/users/5637020'}],
                     'author_detail': {'name': 'huhnmonster',
                                       'href': 'https://stackoverflow.com/users/5637020'},
                     'href': 'https://stackoverflow.com/users/5637020', 'author': 'huhnmonster',
                     'links': [{'rel': 'alternate',
                                'href':
                                    'https://stackoverflow.com/questions/59266166/do-messages-form-coinbase'
                                    '-websocket-full-channel-have-a-constant-format',
                                'type': 'text/html'}], 'published': '2019-12-10T11:27:02Z',
                     'updated': '2019-12-10T18:02:34Z',
                     'summary': '<p>I was wondering whether anyone knows if the JSON message '
                                'format for messages of the \'Full\' websocket channel '
                                'remains constant. That means, does the order of keys ever '
                                'change for whatever reason?</p>\n\n<p>To be more specific ('
                                'for illustration only): \nDoes <code>{"side":"buy", '
                                '"size":"123.123"}</code> ever change to <code>{'
                                '"size":"123.123","side":"buy"}</code> (after server restarts '
                                'on Coinbase side for example?)</p>\n\n<p>I have already '
                                'looked at the format for the past couple of days and did not '
                                'find any deviation, but as this represents only a small '
                                'amount of time, I do not trust it much. I am asking, '
                                'since a constant order would make parsing the messages much '
                                'quicker.</p>\n\n<p>I could not get any information on this '
                                'from their <a '
                                'href="https://docs.pro.coinbase.com/#the-full-channel" '
                                'rel="nofollow noreferrer">documentation</a>.</p>',
                     'summary_detail': {'type': 'text/html', 'language': None,
                                        'base': 'https://stackoverflow.com/feeds/',
                                        'value': '<p>I was wondering whether anyone knows if '
                                                 'the JSON message format for messages of the '
                                                 '\'Full\' websocket channel remains '
                                                 'constant. That means, does the order of '
                                                 'keys ever change for whatever '
                                                 'reason?</p>\n\n<p>To be more specific (for '
                                                 'illustration only): \nDoes <code>{'
                                                 '"side":"buy", "size":"123.123"}</code> ever '
                                                 'change to <code>{"size":"123.123",'
                                                 '"side":"buy"}</code> (after server restarts '
                                                 'on Coinbase side for example?)</p>\n\n<p>I '
                                                 'have already looked at the format for the '
                                                 'past couple of days and did not find any '
                                                 'deviation, but as this represents only a '
                                                 'small amount of time, I do not trust it '
                                                 'much. I am asking, since a constant order '
                                                 'would make parsing the messages much '
                                                 'quicker.</p>\n\n<p>I could not get any '
                                                 'information on this from their <a '
                                                 'href="https://docs.pro.coinbase.com/#the-full-channel" '
                                                 'rel="nofollow noreferrer">documentation</a>.</p>'}},
                    {'id': 'https://stackoverflow.com/q/59206453', 'guidislink': True,
                     'link':
                         'https://stackoverflow.com/questions/59206453/how-to-insert-data-into-mysql'
                         '-with-dynamic-form-like-this',
                     're_rank': {'scheme': 'https://stackoverflow.com'},
                     'title': 'How to insert data into mysql with dynamic form like this',
                     'title_detail': {'type': 'text/plain', 'language': None,
                                      'base': 'https://stackoverflow.com/feeds/',
                                      'value': 'How to insert data into mysql with dynamic '
                                               'form like this'},
                     'tags': [{'term': 'javascript', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None},
                              {'term': 'jquery', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None},
                              {'term': 'html', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None},
                              {'term': 'css', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None},
                              {'term': 'ajax', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None}], 'authors': [{'name': 'neno kusminto',
                                                             'href':
                                                                 'https://stackoverflow.com/users/12483388'}],
                     'author_detail': {'name': 'neno kusminto',
                                       'href': 'https://stackoverflow.com/users/12483388'},
                     'href': 'https://stackoverflow.com/users/12483388',
                     'author': 'neno kusminto',
                     'links': [{'rel': 'alternate',
                                'href':
                                    'https://stackoverflow.com/questions/59206453/how-to-insert-data-into-mysql-with'
                                    '-dynamic-form-like-this',
                                'type': 'text/html'}],
                     'published': '2019-12-06T03:30:26Z',
                     'updated': '2019-12-10T18:02:51Z',
                     'summary': '<p><a href="https://i.stack.imgur.com/Ys4mW.png" '
                                'rel="nofollow noreferrer">this my form</a></p>\n\n<p>My form '
                                'code:</p>\n\n<p><div class="snippet">\n<div '
                                'class="snippet-code">\n<pre class="snippet-code-html '
                                'lang-html prettyprint-override"><code>&lt;script '
                                'src="dist/css/style.css"&gt;&lt;/script&gt;\n&lt;script '
                                'src="dist/js/choosen.js"&gt;&lt;/script&gt;\n\n&lt;?php\ninclude '
                                '"../site.php";\ninclude "../db=connection.php";\n\n$queryjob = '
                                '"SELECT * FROM jobdesk";\n$rsjob=mysqli_query($con,'
                                '$queryjob);\n\n\necho "&lt;div class=\'content-wrapper\'&gt;\n\n '
                                '&lt;div class=\'row\'&gt;\n          &lt;div class=\'col-12\'&gt;\n  '
                                '          &lt;div class=\'card\'&gt;\n              &lt;div '
                                'class=\'card-header\'&gt;\n                &lt;h3 '
                                'class=\'card-title\'&gt;INPUT JOB DESCRIPTION STAFF&lt;/h3&gt;\n     '
                                '           &lt;div class=\'card-tools\'&gt;\n                  '
                                '&lt;div class=\'input-group input-group-sm\' style=\'width: '
                                '150px;\'&gt;\n                    &lt;input type=\'text\' '
                                'name=\'table_search\' class=\'form-control float-right\' '
                                'placeholder=\'Search\'&gt;\n                    \n                   '
                                ' &lt;div class=\'input-group-append\'&gt;\n                      '
                                '&lt;button type=\'submit\' onclick=\'reloadsalary(0,0,'
                                '0)\' class=\'btn btn-default\'&gt;&lt;i class=\'fa '
                                'fa-arrow-left\'&gt;&lt;/i&gt;&lt;/button&gt;\n                    '
                                '&lt;/div&gt;\n                  &lt;/div&gt;\n                '
                                '&lt;/div&gt;\n              &lt;/div&gt;\n              &lt;!-- '
                                '/.card-header --&gt;\n              &lt;div class=\'card-body '
                                'table-responsive p-0\'&gt;\n\n\n              &lt;div class=\'card '
                                'card-primary\' style=\'height:700px;\'&gt;\n              \n         '
                                '     &lt;!-- /.card-header --&gt;\n                &lt;div '
                                'class=\'card-body\'&gt;\n                 &lt;div '
                                'class=\'form-group\' &gt;\n                    '
                                '&lt;label&gt;STAFF&lt;/label&gt;\n                    &lt;select '
                                'class=\'chosen\' name=\'staff\' id=\'staff\' onchange=\'getstaff('
                                'this.value)\' class=\'form-control\'&gt;\n                    '
                                '&lt;option selected=\'selected\' '
                                'value=0&gt;Pilihan&lt;/option&gt;";\n\n                    while('
                                '$rowjob = mysqli_fetch_array($rsjob)){\n                      echo '
                                '"&lt;option value=\'".$rowjob[\'id\']."\'&gt;".$rowjob['
                                '\'nama\']."&lt;/option&gt;";\n                    }\n                '
                                '    echo"&lt;/select&gt;\n                  &lt;/div&gt;\n           '
                                '       &lt;div class=form-group\' name=\'divstaff\' '
                                'id=\'divstaff\'&gt;";\n                  echo "&lt;/div&gt;\n        '
                                '            &lt;button type=\'button\' class=\'btn btn-primary\' '
                                'id=\'but_upload\'&gt;Submit&lt;/button&gt;";\n              echo" \n '
                                '           &lt;/div&gt;        \n              &lt;/div&gt;\n        '
                                '    &lt;/div&gt;\n          &lt;/div&gt;\n        '
                                '&lt;/div&gt;\n&lt;/div&gt;";\n?&gt;\n&lt;script&gt;\n   function '
                                'getstaff(x) {\n    $.ajax({\n      type:\'POST\','
                                '\n      url:\'getSalary.php\',\n      data:{\'staff\':x},'
                                '\n      success:function(data){\n        $(\'#divstaff\').html('
                                'data);\n      }\n    });\n  }\n\n  $(document).ready(function(){\n   '
                                ' $(".chosen").chosen();\n    $("#but_upload").click(function(){\n    '
                                '    var fd = new FormData();\n        var a = '
                                'document.getElementById("staff").options[document.getElementById('
                                '"staff").selectedIndex].value;\n        var h = "";\n      for (var '
                                'i = 1; i &lt;= $("#salaryItem").val(); i++) {\n        if(i==1){\n   '
                                '       h = h + $("#keterangan"+i).val();\n        }\n        else{\n '
                                '         h = h + ";" + $("#keterangan"+i).val();\n        }\n      '
                                '}\n\n        fd.append(\'staff\',a);\n        fd.append('
                                '\'keterangan\',h);\n        $.ajax({\n            url: '
                                '\'insertSalary.php\',\n            type: \'post\',\n            '
                                'data: fd,\n            contentType: false,\n            processData: '
                                'false,\n            success: function(response){\n            \tif('
                                'response=="success"){\n                alert(response);\n            '
                                '\t\treloadPage(-13,0,0);\n            \t}\n            },'
                                '\n        });\n    '
                                '});\n});\n\n&lt;/script&gt;</code></pre>\n</div>\n</div>\n</p>\n\n<p><code'
                                '>getsalary.php</code>:</p>\n\n<p>The following code is get salary.php and there are '
                                'some problems when sending with Ajax</p>\n\n<p><div class="snippet">\n<div '
                                'class="snippet-code">\n<pre class="snippet-code-html lang-html '
                                'prettyprint-override"><code>&lt;?php\ninclude "../site.php";\ninclude '
                                '"../db=connection.php";\n\n$queryjob = "SELECT * FROM jobdesk WHERE id=".$_POST['
                                '\'staff\'];\n$rsjob=mysqli_query($con,$queryjob);\n\nwhile($rowjob = '
                                'mysqli_fetch_array($rsjob)){\n      $data= explode(",",$rowjob[\'job\']);\n      '
                                'for($i=0; $i &lt; count($data); $i++){\n          echo " &lt;div '
                                'class=form-group\'&gt;\n            &lt;label '
                                'style=\'margin-right:85px;\'&gt;&lt;option value=".$data[$i]."&gt;".$data['
                                '$i]."&lt;/option&gt;&lt;/label&gt;\n                &lt;select '
                                'name=\'salaryItem".$i."\' id=\'salaryItem".$i."\' onchange=\'getSalaryItem('
                                'this.value,".$i.")\'&gt;\n                   &lt;option selected=\'selected\' '
                                'value=0&gt;Pilih jumlah Item&lt;/option&gt;";\n      \n                          '
                                'for ($x = 1; $x &lt;= 20; $x++){\n                            echo "&lt;option '
                                'value=".$x."&gt;".$x."&lt;/option&gt;";\n                          }\n\n            '
                                '    echo "&lt;/select&gt;\n                &lt;/div&gt;&lt;/br&gt;\n                '
                                '&lt;div class=form-group\' name=\'divsalary".$i."\' '
                                'id=\'divsalary".$i."\'&gt;&lt;/div&gt;";\n\n                  echo"\n               '
                                '   &lt;/div&gt;";\n                                    }  \n                  '
                                '}\n?&gt;\n&lt;script&gt;\n$(document).ready(function () {\n  $(".chosen").chosen('
                                ');\n})\n\nfunction getSalaryItem(x,y){\n    $.ajax({\n      type:\'POST\','
                                '\n      url:\'getSalary_item.php\',\n      data:{\'salaryItem\':x,\'countItem\':y},'
                                '\n      success:function(data){\n        $(\'#divsalary\'+y).html(data);\n      }\n '
                                '   });\n    \n  } '
                                '\n&lt;/script&gt;</code></pre>\n</div>\n</div>\n</p>\n\n<p><code>salary_item.php'
                                '</code>:</p>\n\n<p><div class="snippet">\n<div class="snippet-code">\n<pre '
                                'class="snippet-code-html lang-html prettyprint-override"><code>&lt;?php\n include '
                                '"../site.php";\n include "../db=connection.php";\n\n $jobdesk = $_POST['
                                '\'jenisgaji\'];\n $jd = $_POST[\'jd\'];\n\n$query3 = "SELECT * FROM jenisgaji WHERE '
                                'id_job=".$jobdesk;\n$rs3=mysqli_query($con,$query3);\n//$row3 = mysqli_fetch_array('
                                '$rs3);\n\n for ($x = 1; $x &lt;= $jd; $x++){\n \t//$query4 = "SELECT * FROM ketSal '
                                'WHERE jenisgaji LIKE \'%".$jobdesk."%\' and flag = 1";\n \t//$rs4=mysqli_query('
                                '$con,$query4);\n \techo"&lt;div class=form-group\' '
                                'style=\'margin-bottom:10px;\'&gt;\n     &lt;label&gt;Job Item '
                                '".$x."&lt;/label&gt;\n     &lt;input type=\'textbox\' required '
                                'class=\'form-control\' name=\'".$jd."keterangan".$x."\' '
                                'id=\'".$jd."keterangan".$x."\' placeholder=\'Ketikkan Keterangan Job disini\'&gt;\n '
                                '    &lt;/input&gt;\n \t&lt;!---- &lt;select class=\'chosen\' '
                                'name=\'keterangan".$x."\' id=\'keterangan".$x."\' style=\'width: 100%;\'&gt;\n '
                                '\t&lt;option selected=\'selected\' value=0&gt;Pilihan&lt;/option&gt; ---&gt;";\n\n '
                                '\n \techo"&lt;/select&gt;&lt;/div&gt;";\n\n }\n\n ?&gt;\n &lt;script&gt;\n \t$('
                                'document).ready(function(){\n \t\t$(".chosen").chosen();\n \t});\n '
                                '&lt;/script&gt;</code></pre>\n</div>\n</div>\n</p>\n\n<p><a '
                                'href="https://i.stack.imgur.com/JT6Qb.png" rel="nofollow noreferrer"><img '
                                'alt="enter image description here" src="https://i.stack.imgur.com/JT6Qb.png" '
                                '/></a></p>',
                     'summary_detail': {'type': 'text/html', 'language': None,
                                        'base': 'https://stackoverflow.com/feeds/',
                                        'value': '<p><a '
                                                 'href="https://i.stack.imgur.com/Ys4mW.png" '
                                                 'rel="nofollow noreferrer">this my '
                                                 'form</a></p>\n\n<p>My form '
                                                 'code:</p>\n\n<p><div class="snippet">\n<div '
                                                 'class="snippet-code">\n<pre '
                                                 'class="snippet-code-html lang-html '
                                                 'prettyprint-override"><code>&lt;script '
                                                 'src="dist/css/style.css"&gt;&lt;/script&gt;\n&lt;script '
                                                 'src="dist/js/choosen.js"&gt;&lt;/script&gt;\n\n&lt;?php\ninclude '
                                                 '"../site.php";\ninclude "../db=connection.php";\n\n$queryjob = '
                                                 '"SELECT * FROM jobdesk";\n$rsjob=mysqli_query($con,'
                                                 '$queryjob);\n\n\necho "&lt;div class=\'content-wrapper\'&gt;\n\n '
                                                 '&lt;div class=\'row\'&gt;\n          &lt;div '
                                                 'class=\'col-12\'&gt;\n            &lt;div class=\'card\'&gt;\n     '
                                                 '         &lt;div class=\'card-header\'&gt;\n                &lt;h3 '
                                                 'class=\'card-title\'&gt;INPUT JOB DESCRIPTION STAFF&lt;/h3&gt;\n   '
                                                 '             &lt;div class=\'card-tools\'&gt;\n                  '
                                                 '&lt;div class=\'input-group input-group-sm\' style=\'width: '
                                                 '150px;\'&gt;\n                    &lt;input type=\'text\' '
                                                 'name=\'table_search\' class=\'form-control float-right\' '
                                                 'placeholder=\'Search\'&gt;\n                    \n                 '
                                                 '   &lt;div class=\'input-group-append\'&gt;\n                      '
                                                 '&lt;button type=\'submit\' onclick=\'reloadsalary(0,0,'
                                                 '0)\' class=\'btn btn-default\'&gt;&lt;i class=\'fa '
                                                 'fa-arrow-left\'&gt;&lt;/i&gt;&lt;/button&gt;\n                    '
                                                 '&lt;/div&gt;\n                  &lt;/div&gt;\n                '
                                                 '&lt;/div&gt;\n              &lt;/div&gt;\n              &lt;!-- '
                                                 '/.card-header --&gt;\n              &lt;div class=\'card-body '
                                                 'table-responsive p-0\'&gt;\n\n\n              &lt;div class=\'card '
                                                 'card-primary\' style=\'height:700px;\'&gt;\n              \n       '
                                                 '       &lt;!-- /.card-header --&gt;\n                &lt;div '
                                                 'class=\'card-body\'&gt;\n                 &lt;div '
                                                 'class=\'form-group\' &gt;\n                    '
                                                 '&lt;label&gt;STAFF&lt;/label&gt;\n                    &lt;select '
                                                 'class=\'chosen\' name=\'staff\' id=\'staff\' onchange=\'getstaff('
                                                 'this.value)\' class=\'form-control\'&gt;\n                    '
                                                 '&lt;option selected=\'selected\' '
                                                 'value=0&gt;Pilihan&lt;/option&gt;";\n\n                    while('
                                                 '$rowjob = mysqli_fetch_array($rsjob)){\n                      echo '
                                                 '"&lt;option value=\'".$rowjob[\'id\']."\'&gt;".$rowjob['
                                                 '\'nama\']."&lt;/option&gt;";\n                    }\n              '
                                                 '      echo"&lt;/select&gt;\n                  &lt;/div&gt;\n       '
                                                 '           &lt;div class=form-group\' name=\'divstaff\' '
                                                 'id=\'divstaff\'&gt;";\n                  echo "&lt;/div&gt;\n      '
                                                 '              &lt;button type=\'button\' class=\'btn btn-primary\' '
                                                 'id=\'but_upload\'&gt;Submit&lt;/button&gt;";\n              echo" '
                                                 '\n            &lt;/div&gt;        \n              &lt;/div&gt;\n   '
                                                 '         &lt;/div&gt;\n          &lt;/div&gt;\n        '
                                                 '&lt;/div&gt;\n&lt;/div&gt;";\n?&gt;\n&lt;script&gt;\n   function '
                                                 'getstaff(x) {\n    $.ajax({\n      type:\'POST\','
                                                 '\n      url:\'getSalary.php\',\n      data:{\'staff\':x},'
                                                 '\n      success:function(data){\n        $(\'#divstaff\').html('
                                                 'data);\n      }\n    });\n  }\n\n  $(document).ready(function(){\n '
                                                 '   $(".chosen").chosen();\n    $("#but_upload").click(function(){'
                                                 '\n        var fd = new FormData();\n        var a = '
                                                 'document.getElementById("staff").options[document.getElementById('
                                                 '"staff").selectedIndex].value;\n        var h = "";\n      for ('
                                                 'var i = 1; i &lt;= $("#salaryItem").val(); i++) {\n        if('
                                                 'i==1){\n          h = h + $("#keterangan"+i).val();\n        }\n   '
                                                 '     else{\n          h = h + ";" + $("#keterangan"+i).val();\n    '
                                                 '    }\n      }\n\n        fd.append(\'staff\',a);\n        '
                                                 'fd.append(\'keterangan\',h);\n        $.ajax({\n            url: '
                                                 '\'insertSalary.php\',\n            type: \'post\',\n            '
                                                 'data: fd,\n            contentType: false,\n            '
                                                 'processData: false,\n            success: function(response){\n    '
                                                 '        \tif(response=="success"){\n                alert('
                                                 'response);\n            \t\treloadPage(-13,0,0);\n            '
                                                 '\t}\n            },\n        });\n    '
                                                 '});\n});\n\n&lt;/script&gt;</code></pre>\n</div>\n</div>\n</p>\n\n'
                                                 '<p><code>getsalary.php</code>:</p>\n\n<p>The following code is get '
                                                 'salary.php and there are some problems when sending with '
                                                 'Ajax</p>\n\n<p><div class="snippet">\n<div '
                                                 'class="snippet-code">\n<pre class="snippet-code-html lang-html '
                                                 'prettyprint-override"><code>&lt;?php\ninclude '
                                                 '"../site.php";\ninclude "../db=connection.php";\n\n$queryjob = '
                                                 '"SELECT * FROM jobdesk WHERE id=".$_POST['
                                                 '\'staff\'];\n$rsjob=mysqli_query($con,$queryjob);\n\nwhile($rowjob '
                                                 '= mysqli_fetch_array($rsjob)){\n      $data= explode(",",'
                                                 '$rowjob[\'job\']);\n      for($i=0; $i &lt; count($data); $i++){\n '
                                                 '         echo " &lt;div class=form-group\'&gt;\n            '
                                                 '&lt;label style=\'margin-right:85px;\'&gt;&lt;option '
                                                 'value=".$data[$i]."&gt;".$data['
                                                 '$i]."&lt;/option&gt;&lt;/label&gt;\n                &lt;select '
                                                 'name=\'salaryItem".$i."\' id=\'salaryItem".$i."\' '
                                                 'onchange=\'getSalaryItem(this.value,".$i.")\'&gt;\n                '
                                                 '   &lt;option selected=\'selected\' value=0&gt;Pilih jumlah '
                                                 'Item&lt;/option&gt;";\n      \n                          for ($x = '
                                                 '1; $x &lt;= 20; $x++){\n                            echo '
                                                 '"&lt;option value=".$x."&gt;".$x."&lt;/option&gt;";\n              '
                                                 '            }\n\n                echo "&lt;/select&gt;\n           '
                                                 '     &lt;/div&gt;&lt;/br&gt;\n                &lt;div '
                                                 'class=form-group\' name=\'divsalary".$i."\' '
                                                 'id=\'divsalary".$i."\'&gt;&lt;/div&gt;";\n\n                  '
                                                 'echo"\n                  &lt;/div&gt;";\n                          '
                                                 '          }  \n                  }\n?&gt;\n&lt;script&gt;\n$('
                                                 'document).ready(function () {\n  $(".chosen").chosen('
                                                 ');\n})\n\nfunction getSalaryItem(x,y){\n    $.ajax({\n      '
                                                 'type:\'POST\',\n      url:\'getSalary_item.php\',\n      data:{'
                                                 '\'salaryItem\':x,\'countItem\':y},\n      success:function(data){'
                                                 '\n        $(\'#divsalary\'+y).html(data);\n      }\n    });\n    '
                                                 '\n  } '
                                                 '\n&lt;/script&gt;</code></pre>\n</div>\n</div>\n</p>\n\n<p><code>'
                                                 'salary_item.php</code>:</p>\n\n<p><div class="snippet">\n<div '
                                                 'class="snippet-code">\n<pre class="snippet-code-html lang-html '
                                                 'prettyprint-override"><code>&lt;?php\n include "../site.php";\n '
                                                 'include "../db=connection.php";\n\n $jobdesk = $_POST['
                                                 '\'jenisgaji\'];\n $jd = $_POST[\'jd\'];\n\n$query3 = "SELECT * '
                                                 'FROM jenisgaji WHERE id_job=".$jobdesk;\n$rs3=mysqli_query($con,'
                                                 '$query3);\n//$row3 = mysqli_fetch_array($rs3);\n\n for ($x = 1; $x '
                                                 '&lt;= $jd; $x++){\n \t//$query4 = "SELECT * FROM ketSal WHERE '
                                                 'jenisgaji LIKE \'%".$jobdesk."%\' and flag = 1";\n '
                                                 '\t//$rs4=mysqli_query($con,$query4);\n \techo"&lt;div '
                                                 'class=form-group\' style=\'margin-bottom:10px;\'&gt;\n     '
                                                 '&lt;label&gt;Job Item ".$x."&lt;/label&gt;\n     &lt;input '
                                                 'type=\'textbox\' required class=\'form-control\' '
                                                 'name=\'".$jd."keterangan".$x."\' id=\'".$jd."keterangan".$x."\' '
                                                 'placeholder=\'Ketikkan Keterangan Job disini\'&gt;\n     '
                                                 '&lt;/input&gt;\n \t&lt;!---- &lt;select class=\'chosen\' '
                                                 'name=\'keterangan".$x."\' id=\'keterangan".$x."\' style=\'width: '
                                                 '100%;\'&gt;\n \t&lt;option selected=\'selected\' '
                                                 'value=0&gt;Pilihan&lt;/option&gt; ---&gt;";\n\n \n '
                                                 '\techo"&lt;/select&gt;&lt;/div&gt;";\n\n }\n\n ?&gt;\n '
                                                 '&lt;script&gt;\n \t$(document).ready(function(){\n \t\t$('
                                                 '".chosen").chosen();\n \t});\n '
                                                 '&lt;/script&gt;</code></pre>\n</div>\n</div>\n</p>\n\n<p><a '
                                                 'href="https://i.stack.imgur.com/JT6Qb.png" rel="nofollow '
                                                 'noreferrer"><img alt="enter image description here" '
                                                 'src="https://i.stack.imgur.com/JT6Qb.png" /></a></p>'}},
                    {'id': 'https://stackoverflow.com/q/59196064', 'guidislink': True,
                     'link':
                         'https://stackoverflow.com/questions/59196064/css-keyframes-animation-is-not'
                         '-smooth-on-safari-but-works-on-chrome',
                     're_rank': {'scheme': 'https://stackoverflow.com'},
                     'title': 'CSS keyframes animation is not smooth on Safari but works on '
                              'Chrome',
                     'title_detail': {'type': 'text/plain', 'language': None,
                                      'base': 'https://stackoverflow.com/feeds/',
                                      'value': 'CSS keyframes animation is not smooth on '
                                               'Safari but works on Chrome'},
                     'tags': [{'term': 'html', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None},
                              {'term': 'css', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None}], 'authors': [
                        {'name': 'dennis', 'href': 'https://stackoverflow.com/users/865431'}],
                     'author_detail': {'name': 'dennis',
                                       'href': 'https://stackoverflow.com/users/865431'},
                     'href': 'https://stackoverflow.com/users/865431', 'author': 'dennis',
                     'links': [{'rel': 'alternate',
                                'href':
                                    'https://stackoverflow.com/questions/59196064/css-keyframes-animation-is-not'
                                    '-smooth-on-safari-but-works-on-chrome',
                                'type': 'text/html'}], 'published': '2019-12-05T13:17:48Z',
                     'updated': '2019-12-10T18:03:00Z',
                     'summary': '<p>I am trying to add a smooth pulsating border to a button '
                                'and it works fine on Chrome but the animation is not smooth '
                                'but you can see the discrete steps of the animation. From '
                                'other StackOverflow questions it looks like this might be a '
                                'performance issue and needs to be solved differently. Just '
                                'trying to make sure I am not overlooking anything with the '
                                'current approach.</p>\n\n<p>It basically looks like '
                                'this:</p>\n\n<p><div class="snippet">\n<div '
                                'class="snippet-code">\n<pre class="snippet-code-css lang-css '
                                'prettyprint-override"><code>.pulse {\n  border-radius: '
                                '7.5px;\n  animation: border-pulsate 2s '
                                'infinite;\n}\n\n@keyframes border-pulsate {\n  0% {\n    '
                                'box-shadow: 0 0 0 1px blue;\n  }\n  50% {\n    box-shadow: 0 '
                                '0 0 3px blue;\n  }\n  100% {\n    box-shadow: 0 0 0 1px '
                                'blue;\n  }\n}</code></pre>\n<pre class="snippet-code-html '
                                'lang-html prettyprint-override"><code>&lt;div&gt;\n  '
                                '&lt;span '
                                'class="pulse"&gt;Pulse&lt;/span&gt;\n&lt;/div&gt;</code></pre>\n</div>\n</div>\n</p>',
                     'summary_detail': {'type': 'text/html', 'language': None,
                                        'base': 'https://stackoverflow.com/feeds/',
                                        'value': '<p>I am trying to add a smooth pulsating '
                                                 'border to a button and it works fine on '
                                                 'Chrome but the animation is not smooth but '
                                                 'you can see the discrete steps of the '
                                                 'animation. From other StackOverflow '
                                                 'questions it looks like this might be a '
                                                 'performance issue and needs to be solved '
                                                 'differently. Just trying to make sure I am '
                                                 'not overlooking anything with the current '
                                                 'approach.</p>\n\n<p>It basically looks like '
                                                 'this:</p>\n\n<p><div class="snippet">\n<div '
                                                 'class="snippet-code">\n<pre '
                                                 'class="snippet-code-css lang-css '
                                                 'prettyprint-override"><code>.pulse {\n  '
                                                 'border-radius: 7.5px;\n  animation: '
                                                 'border-pulsate 2s '
                                                 'infinite;\n}\n\n@keyframes border-pulsate {'
                                                 '\n  0% {\n    box-shadow: 0 0 0 1px blue;\n '
                                                 ' }\n  50% {\n    box-shadow: 0 0 0 3px '
                                                 'blue;\n  }\n  100% {\n    box-shadow: 0 0 0 '
                                                 '1px blue;\n  }\n}</code></pre>\n<pre '
                                                 'class="snippet-code-html lang-html '
                                                 'prettyprint-override"><code>&lt;div&gt;\n  '
                                                 '&lt;span '
                                                 'class="pulse"&gt;Pulse&lt;/span&gt;\n&lt;/div&gt;</code></pre>\n'
                                                 '</div>\n</div>\n</p>'}},
                    {'id': 'https://stackoverflow.com/q/59182519', 'guidislink': True,
                     'link':
                         'https://stackoverflow.com/questions/59182519/change-default-connection'
                         '-dynamically',
                     're_rank': {'scheme': 'https://stackoverflow.com'},
                     'title': 'Change default connection dynamically',
                     'title_detail': {'type': 'text/plain', 'language': None,
                                      'base': 'https://stackoverflow.com/feeds/',
                                      'value': 'Change default connection dynamically'},
                     'tags': [{'term': 'php', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None},
                              {'term': 'mysql', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None},
                              {'term': 'database', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None},
                              {'term': 'laravel', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None},
                              {'term': 'connection', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None}], 'authors': [{'name': 'Vincenzo',
                                                             'href':
                                                                 'https://stackoverflow.com/users/12457271'}],
                     'author_detail': {'name': 'Vincenzo',
                                       'href': 'https://stackoverflow.com/users/12457271'},
                     'href': 'https://stackoverflow.com/users/12457271', 'author': 'Vincenzo',
                     'links': [{'rel': 'alternate',
                                'href':
                                    'https://stackoverflow.com/questions/59182519/change-default-connection'
                                    '-dynamically',
                                'type': 'text/html'}], 'published': '2019-12-04T18:23:42Z',
                     'updated': '2019-12-10T18:03:12Z',
                     'summary': '<p>I have a middleware in Laravel application that change '
                                'database connection dynamically:</p>\n\n<pre><code>public '
                                'function handle($request, Closure $next)\n{\n    '
                                'Config::set(\'database.default\', '
                                '\'mysql_\'.$request-&gt;segment(1));\n    DB::reconnect('
                                '\'mysql_\'.$request-&gt;segment(1));\n    app('
                                ')-&gt;setLocale($request-&gt;segment(1));\n    if ('
                                'Auth::check() &amp;&amp; session(\'locale\') != '
                                '$request-&gt;segment(1))\n    {\n        Auth::logout();\n   '
                                '     return redirect(\'login\');\n    }\n    return $next('
                                '$request);\n}\n</code></pre>\n\n<p>This work, the default '
                                'connection change but the model connection stey the '
                                'old.</p>\n\n<p>In dump of a model I '
                                'have:</p>\n\n<p>"mysql_es" is default connection changed by '
                                'url segment (/es)</p>\n\n<p>"mysql_it" is a old default '
                                'connection before change by middleware.</p>\n\n<p>can anyone '
                                'tell me why?</p>\n\n<p>Thanks</p>',
                     'summary_detail': {'type': 'text/html', 'language': None,
                                        'base': 'https://stackoverflow.com/feeds/',
                                        'value': '<p>I have a middleware in Laravel '
                                                 'application that change database connection '
                                                 'dynamically:</p>\n\n<pre><code>public '
                                                 'function handle($request, Closure $next)\n{'
                                                 '\n    Config::set(\'database.default\', '
                                                 '\'mysql_\'.$request-&gt;segment(1));\n    '
                                                 'DB::reconnect('
                                                 '\'mysql_\'.$request-&gt;segment(1));\n    '
                                                 'app()-&gt;setLocale($request-&gt;segment('
                                                 '1));\n    if (Auth::check() &amp;&amp; '
                                                 'session(\'locale\') != '
                                                 '$request-&gt;segment(1))\n    {\n        '
                                                 'Auth::logout();\n        return redirect('
                                                 '\'login\');\n    }\n    return $next('
                                                 '$request);\n}\n</code></pre>\n\n<p>This '
                                                 'work, the default connection change but the '
                                                 'model connection stey the old.</p>\n\n<p>In '
                                                 'dump of a model I '
                                                 'have:</p>\n\n<p>"mysql_es" is default '
                                                 'connection changed by url segment ('
                                                 '/es)</p>\n\n<p>"mysql_it" is a old default '
                                                 'connection before change by '
                                                 'middleware.</p>\n\n<p>can anyone tell me '
                                                 'why?</p>\n\n<p>Thanks</p>'}},
                    {'id': 'https://stackoverflow.com/q/59182508', 'guidislink': True,
                     'link':
                         'https://stackoverflow.com/questions/59182508/render-a-function-inside-a'
                         '-component-in-react-js',
                     're_rank': {'scheme': 'https://stackoverflow.com'},
                     'title': 'Render a function inside a component in react js',
                     'title_detail': {'type': 'text/plain', 'language': None,
                                      'base': 'https://stackoverflow.com/feeds/',
                                      'value': 'Render a function inside a component in react '
                                               'js'},
                     'tags': [{'term': 'javascript', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None},
                              {'term': 'reactjs', 'scheme': 'https://stackoverflow.com/tags',
                               'label': None}], 'authors': [
                        {'name': 'Asking', 'href': 'https://stackoverflow.com/users/10201522'}],
                     'author_detail': {'name': 'Asking',
                                       'href': 'https://stackoverflow.com/users/10201522'},
                     'href': 'https://stackoverflow.com/users/10201522', 'author': 'Asking',
                     'links': [{'rel': 'alternate',
                                'href':
                                    'https://stackoverflow.com/questions/59182508/render-a-function-inside-a'
                                    '-component-in-react-js',
                                'type': 'text/html'}], 'published': '2019-12-04T18:23:03Z',
                     'updated': '2019-12-10T18:03:41Z',
                     'summary': '<p>My target is to create a breadcrumb component in react '
                                'js. I used Ant Design in my App, but I have some issues. '
                                '</p>\n\n<p>In the documentation of Ant Design i found a '
                                'solution for creating dynamic breadcrumbs, but can\'t find '
                                'out how to apply the code.</p>\n\n<p>So, at the end I have '
                                'this code: </p>\n\n<p><div class="snippet">\n<div '
                                'class="snippet-code">\n<pre class="snippet-code-js lang-js '
                                'prettyprint-override"><code>import React from '
                                '"react";\nimport {Link, BrowserRouter, Route} from '
                                '"react-router-dom";\nimport {Breadcrumb} from '
                                '\'antd\';\n\n//from here starts the code from Ant Design '
                                'Documentation\nconst routes = [\n    {\n        path: '
                                '\'index\',\n        breadcrumbName: \'home\',\n    },'
                                '\n    {\n        path: \'first\',\n        breadcrumbName: '
                                '\'first\',\n        children: [\n            {\n             '
                                '   path: \'/general\',\n                breadcrumbName: '
                                '\'General\',\n            },\n            {\n                '
                                'path: \'/layout\',\n                breadcrumbName: '
                                '\'Layout\',\n            },\n            {\n                '
                                'path: \'/navigation\',\n                breadcrumbName: '
                                '\'Navigation\',\n            },\n        ],\n    },'
                                '\n    {\n        path: \'second\',\n        breadcrumbName: '
                                '\'second\',\n    },\n];\n\nfunction itemRender(route, '
                                'params, routes, paths) {\n    const last = routes.indexOf('
                                'route) === routes.length - 1;\n    return last ? (\n        '
                                '&lt;span&gt;{route.breadcrumbName}&lt;/span&gt;\n    ) : (\n '
                                '       &lt;Link to={paths.join(\'/\')}&gt;{'
                                'route.breadcrumbName}&lt;/Link&gt;\n    );\n}\nreturn '
                                '&lt;Breadcrumb itemRender={itemRender} routes={routes} '
                                '/&gt;;\n//here is the end of the code from Ant '
                                'Design\n\nfunction App() {\n    return (\n        '
                                '&lt;div&gt;\n            &lt;p&gt;here i want to render my '
                                'breadcrumb&lt;/p&gt;\n        &lt;/div&gt;\n    '
                                ');\n}\n\nexport default '
                                'App;</code></pre>\n</div>\n</div>\n</p>\n\n<p>Also, '
                                'the return statement is located outside of the function and '
                                'i get error due of this.</p>\n\n<p>How to create, '
                                'using this implementation, a breadcrumb, and how to render '
                                '<code>itemRender</code> function inside my component, '
                                'and from where should i get these params <code>itemRender('
                                'route, params, routes, paths)</code>?</p>',
                     'summary_detail': {'type': 'text/html', 'language': None,
                                        'base': 'https://stackoverflow.com/feeds/',
                                        'value': '<p>My target is to create a breadcrumb '
                                                 'component in react js. I used Ant Design in '
                                                 'my App, but I have some issues. '
                                                 '</p>\n\n<p>In the documentation of Ant '
                                                 'Design i found a solution for creating '
                                                 'dynamic breadcrumbs, but can\'t find out '
                                                 'how to apply the code.</p>\n\n<p>So, '
                                                 'at the end I have this code: '
                                                 '</p>\n\n<p><div class="snippet">\n<div '
                                                 'class="snippet-code">\n<pre '
                                                 'class="snippet-code-js lang-js '
                                                 'prettyprint-override"><code>import React '
                                                 'from "react";\nimport {Link, BrowserRouter, '
                                                 'Route} from "react-router-dom";\nimport {'
                                                 'Breadcrumb} from \'antd\';\n\n//from here '
                                                 'starts the code from Ant Design '
                                                 'Documentation\nconst routes = [\n    {\n    '
                                                 '    path: \'index\',\n        '
                                                 'breadcrumbName: \'home\',\n    },'
                                                 '\n    {\n        path: \'first\','
                                                 '\n        breadcrumbName: \'first\','
                                                 '\n        children: [\n            {\n      '
                                                 '          path: \'/general\',\n             '
                                                 '   breadcrumbName: \'General\',\n           '
                                                 ' },\n            {\n                path: '
                                                 '\'/layout\',\n                '
                                                 'breadcrumbName: \'Layout\',\n            },'
                                                 '\n            {\n                path: '
                                                 '\'/navigation\',\n                '
                                                 'breadcrumbName: \'Navigation\',\n           '
                                                 ' },\n        ],\n    },\n    {\n        '
                                                 'path: \'second\',\n        breadcrumbName: '
                                                 '\'second\',\n    },\n];\n\nfunction '
                                                 'itemRender(route, params, routes, '
                                                 'paths) {\n    const last = routes.indexOf('
                                                 'route) === routes.length - 1;\n    return '
                                                 'last ? (\n        &lt;span&gt;{'
                                                 'route.breadcrumbName}&lt;/span&gt;\n    ) : '
                                                 '(\n        &lt;Link to={paths.join('
                                                 '\'/\')}&gt;{'
                                                 'route.breadcrumbName}&lt;/Link&gt;\n    '
                                                 ');\n}\nreturn &lt;Breadcrumb itemRender={'
                                                 'itemRender} routes={routes} /&gt;;\n//here '
                                                 'is the end of the code from Ant '
                                                 'Design\n\nfunction App() {\n    return (\n  '
                                                 '      &lt;div&gt;\n            '
                                                 '&lt;p&gt;here i want to render my '
                                                 'breadcrumb&lt;/p&gt;\n        '
                                                 '&lt;/div&gt;\n    );\n}\n\nexport default '
                                                 'App;</code></pre>\n</div>\n</div>\n</p>\n\n<p>Also, '
                                                 'the return statement is located outside of the '
                                                 'function and i get error due of this.</p>\n\n<p>How '
                                                 'to create, using this implementation, a breadcrumb, '
                                                 'and how to render <code>itemRender</code> function '
                                                 'inside my component, and from where should i get '
                                                 'these params <code>itemRender(route, params, '
                                                 'routes, paths)</code>?</p>'}}],
        'feed': {'title': 'Recent Questions - Stack Overflow',
                 'title_detail': {'type': 'text/plain', 'language': None,
                                  'base': 'https://stackoverflow.com/feeds/',
                                  'value': 'Recent Questions - Stack Overflow'},
                 'links': [
                     {'rel': 'self', 'href': 'https://stackoverflow.com/feeds/', 'type': 'application/atom+xml'},
                     {'rel': 'alternate', 'href': 'https://stackoverflow.com/questions', 'type': 'text/html'},
                     {'rel': 'license', 'href': 'https://creativecommons.org/licenses/by-sa/4.0/rdf'}],
                 'link': 'https://stackoverflow.com/questions',
                 'subtitle': 'most recent 30 from stackoverflow.com',
                 'subtitle_detail': {'type': 'text/plain', 'language': None,
                                     'base': 'https://stackoverflow.com/feeds/',
                                     'value': 'most recent 30 from stackoverflow.com'},
                 'updated': '2019-12-10T18:05:02Z',
                 'id': 'https://stackoverflow.com/feeds/', 'guidislink': False},
        'headers': {'cache-control': 'max-age=120', 'content-type': 'application/atom+xml; charset=utf-8',
                    'expires': 'Tue, 10 Dec 2019 18:07:02 GMT',
                    'last-modified': 'Tue, 10 Dec 2019 18:05:02 GMT', 'x-frame-options': 'SAMEORIGIN',
                    'x-request-guid': '15e71beb-6c58-4b70-856e-0e96f28bf869',
                    'strict-transport-security': 'max-age=15552000',
                    'feature-policy': "microphone 'none'; speaker 'none'",
                    'content-security-policy': "upgrade-insecure-requests; frame-ancestors 'self' "
                                               "https://stackexchange.com",
                    'content-length': '79001', 'accept-ranges': 'bytes',
                    'date': 'Tue, 10 Dec 2019 18:05:03 GMT', 'via': '1.1 varnish', 'age': '0',
                    'connection': 'close', 'x-served-by': 'cache-hhn4073-HHN', 'x-cache': 'MISS',
                    'x-cache-hits': '0', 'x-timer': 'S1576001103.937581,VS0,VE267', 'vary': 'Fastly-SSL',
                    'x-dns-prefetch-control': 'off',
                    'set-cookie': 'prov=20766700-6749-4839-d5c2-57afe3796218; domain=.stackoverflow.com; '
                                  'expires=Fri, 01-Jan-2055 00:00:00 GMT; path=/; HttpOnly'},
        'updated': 'Tue, 10 Dec 2019 18:05:02 GMT',
        'href': 'https://stackoverflow.com/feeds/', 'status': 200, 'encoding': 'utf-8', 'version': 'atom10',
        'namespaces': {'': 'http://www.w3.org/2005/Atom',
                       'creativeCommons': 'http://backend.userland.com/creativeCommonsRssModule',
                       're': 'http://purl.org/atompub/rank/1.0'}}
