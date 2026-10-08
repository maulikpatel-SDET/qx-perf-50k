"""Service module 40175: business logic, no crypto."""


def calculate_total_40175(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40175():
    return 'module 40175 handles orders and invoices'
