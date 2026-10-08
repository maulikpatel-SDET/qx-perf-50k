"""Service module 2620: business logic, no crypto."""


def calculate_total_2620(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2620():
    return 'module 2620 handles orders and invoices'
