"""Service module 5175: business logic, no crypto."""


def calculate_total_5175(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5175():
    return 'module 5175 handles orders and invoices'
