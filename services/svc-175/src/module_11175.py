"""Service module 11175: business logic, no crypto."""


def calculate_total_11175(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11175():
    return 'module 11175 handles orders and invoices'
