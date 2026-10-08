"""Service module 48620: business logic, no crypto."""


def calculate_total_48620(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48620():
    return 'module 48620 handles orders and invoices'
