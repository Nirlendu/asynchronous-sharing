from django.shortcuts import render
from react.render import render_component
from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def react_webpack_test(request):
	return render(request, "test/react-webpack-test.html", {})


@ensure_csrf_cookie
def react_pre_render_test(request):
	# Render HTML output by React server
	rendered_html = render_component(
		'js/component/main.js',
		 props = [],
	)
	return render(request, "test/react-pre-render.html", {})





