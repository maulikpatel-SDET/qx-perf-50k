"""Service module 6175: business logic, no crypto."""


def calculate_total_6175(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6175():
    return 'module 6175 handles orders and invoices'
