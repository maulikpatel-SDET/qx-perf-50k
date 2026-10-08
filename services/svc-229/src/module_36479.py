"""Service module 36479: business logic, no crypto."""


def calculate_total_36479(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36479():
    return 'module 36479 handles orders and invoices'
