"""Service module 27175: business logic, no crypto."""


def calculate_total_27175(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27175():
    return 'module 27175 handles orders and invoices'
