"""Service module 43603: business logic, no crypto."""


def calculate_total_43603(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43603():
    return 'module 43603 handles orders and invoices'
