"""Service module 3620: business logic, no crypto."""


def calculate_total_3620(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3620():
    return 'module 3620 handles orders and invoices'
