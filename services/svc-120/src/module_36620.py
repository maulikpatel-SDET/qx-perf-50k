"""Service module 36620: business logic, no crypto."""


def calculate_total_36620(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36620():
    return 'module 36620 handles orders and invoices'
