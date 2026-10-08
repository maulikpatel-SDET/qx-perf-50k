"""Service module 38620: business logic, no crypto."""


def calculate_total_38620(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38620():
    return 'module 38620 handles orders and invoices'
