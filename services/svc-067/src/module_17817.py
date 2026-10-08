"""Service module 17817: business logic, no crypto."""


def calculate_total_17817(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17817():
    return 'module 17817 handles orders and invoices'
