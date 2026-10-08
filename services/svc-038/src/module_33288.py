"""Service module 33288: business logic, no crypto."""


def calculate_total_33288(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33288():
    return 'module 33288 handles orders and invoices'
