"""Service module 22423: business logic, no crypto."""


def calculate_total_22423(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22423():
    return 'module 22423 handles orders and invoices'
