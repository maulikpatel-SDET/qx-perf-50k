"""Service module 30620: business logic, no crypto."""


def calculate_total_30620(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30620():
    return 'module 30620 handles orders and invoices'
