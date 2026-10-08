"""Service module 39175: business logic, no crypto."""


def calculate_total_39175(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39175():
    return 'module 39175 handles orders and invoices'
