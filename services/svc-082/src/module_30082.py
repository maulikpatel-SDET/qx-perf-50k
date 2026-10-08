"""Service module 30082: business logic, no crypto."""


def calculate_total_30082(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30082():
    return 'module 30082 handles orders and invoices'
