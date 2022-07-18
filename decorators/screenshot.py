import functools
from mimetypes import MimeTypes
from test_base.web_driver_factory import WebDriverFactory
from qaseio.pytest import qase

class screenshot:
    def on_failure(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception:
                qase.attach(
                    (WebDriverFactory.get_driver().get_screenshot_as_png(), "image/png", "test-failure.png")
                )
                raise
        return wrapper