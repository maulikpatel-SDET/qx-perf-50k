"""Service module 9729: business logic, no crypto."""


def calculate_total_9729(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9729():
    return 'module 9729 handles orders and invoices'
