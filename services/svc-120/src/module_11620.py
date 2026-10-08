"""Service module 11620: business logic, no crypto."""


def calculate_total_11620(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11620():
    return 'module 11620 handles orders and invoices'
