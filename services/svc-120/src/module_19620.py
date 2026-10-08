"""Service module 19620: business logic, no crypto."""


def calculate_total_19620(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19620():
    return 'module 19620 handles orders and invoices'
