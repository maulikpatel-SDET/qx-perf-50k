"""Service module 14175: business logic, no crypto."""


def calculate_total_14175(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14175():
    return 'module 14175 handles orders and invoices'
