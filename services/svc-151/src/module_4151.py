"""Service module 4151: business logic, no crypto."""


def calculate_total_4151(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4151():
    return 'module 4151 handles orders and invoices'
