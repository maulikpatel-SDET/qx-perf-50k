"""Service module 39169: business logic, no crypto."""


def calculate_total_39169(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39169():
    return 'module 39169 handles orders and invoices'
