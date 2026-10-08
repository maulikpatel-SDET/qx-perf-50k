"""Service module 34220: business logic, no crypto."""


def calculate_total_34220(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34220():
    return 'module 34220 handles orders and invoices'
