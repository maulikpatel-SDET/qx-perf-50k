"""Service module 41175: business logic, no crypto."""


def calculate_total_41175(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41175():
    return 'module 41175 handles orders and invoices'
