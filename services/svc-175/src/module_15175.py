"""Service module 15175: business logic, no crypto."""


def calculate_total_15175(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15175():
    return 'module 15175 handles orders and invoices'
