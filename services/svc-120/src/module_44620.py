"""Service module 44620: business logic, no crypto."""


def calculate_total_44620(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44620():
    return 'module 44620 handles orders and invoices'
