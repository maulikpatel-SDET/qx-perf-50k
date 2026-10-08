"""Service module 47573: business logic, no crypto."""


def calculate_total_47573(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47573():
    return 'module 47573 handles orders and invoices'
