itunes-iap v2
~~~~~~~~~~~~~

.. image:: https://travis-ci.org/youknowone/itunes-iap.svg?branch=master
    :target: https://travis-ci.org/youknowone/itunes-iap


IMPORTANT
-----------------
This branch removes the global stack, I was in a hurry, so I did not update the tests.
I required the change, because I needed to run the IAP-Validation in a multithreaded environment.

To do validation, simply do:

    >>> import itunesiap
    >>> print itunesiap.env.sandbox.verify(raw_data)
    >>> print itunesiap.env.production.verify(raw_data)



Note for v1 users
-----------------

There was breaking changes between v1 and v2 APIs.

- Specify version `0.6.6` for latest v1 API when you don't need new APIs.
- Or use `import itunesiap.legacy as itunesiap` instead of `import itunesiap`. (`from itunesiap import xxx` to `from itunesiap.legacy import xxx`)

Quick example
-------------

Create request to create a request to itunes verify api.

    >>> import itunesiap
    >>> try:
    >>>     response = itunesiap.verify(raw_data)  # base64-encoded data
    >>> except itunesiap.exc.InvalidReceipt as e:
    >>>     print('invalid receipt')
    >>> print response.receipt.last_in_app.product_id  # other values are also available as property!

Practical values are: product_id, original_transaction_id, quantity, unique_identifier

Quick example with password (Apple Shared Secret)
-------------------------------------------------

Create request to create a request to itunes verify api.

    >>> import itunesiap
    >>> try:
    >>>     response = itunesiap.verify(raw_data, password)  # Just add password
    >>> except itunesiap.exc.InvalidReceipt as e:
    >>>     print('invalid receipt')
    >>> in_app = response.receipt.last_in_app  # Get the latest receipt returned by Apple


Verification policy
-------------------

Set verification mode for production or sandbox api. Review mode also available for appstore review.

    >>> import itunesiap
    >>> with itunesiap.env.review:
    >>>     response = itunesiap.verify(raw_data)  # `review` enables both production and sandbox for appstore review. `production`, `sandbox`, `review` or `default` possible.

Or

    >>> import itunesiap
    >>> itunesiap.env.review.push()  # explicitly pushed context
    >>> response = request.verify()

Or

    >>> import itunesiap
    >>> with itunesiap.env.current().clone(use_sandbox=True):  # additional change for current environment.
    >>>     response = itunesiap.verify(raw_data)

Proxy
-----

Put `proxy_url` for proxies.

    >>> import itunesiap
    >>> try:
    >>>     response = itunesiap.verify(raw_data, proxy_url='https://your.proxy.url/')
    >>> except itunesiap.exc.InvalidReceipt as e:
    >>>     ...

Contributors
------------

See https://github.com/youknowone/itunes-iap/graphs/contributors
