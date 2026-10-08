"""Service module 39307: business logic, no crypto."""


def calculate_total_39307(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39307():
    return 'module 39307 handles orders and invoices'
