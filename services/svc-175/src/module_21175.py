"""Service module 21175: business logic, no crypto."""


def calculate_total_21175(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21175():
    return 'module 21175 handles orders and invoices'
