"""Service module 175: business logic, no crypto."""


def calculate_total_175(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_175():
    return 'module 175 handles orders and invoices'
