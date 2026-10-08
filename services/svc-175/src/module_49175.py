"""Service module 49175: business logic, no crypto."""


def calculate_total_49175(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49175():
    return 'module 49175 handles orders and invoices'
