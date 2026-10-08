"""Service module 620: business logic, no crypto."""


def calculate_total_620(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_620():
    return 'module 620 handles orders and invoices'
