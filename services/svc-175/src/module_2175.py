"""Service module 2175: business logic, no crypto."""


def calculate_total_2175(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2175():
    return 'module 2175 handles orders and invoices'
