"""Service module 24209: business logic, no crypto."""


def calculate_total_24209(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24209():
    return 'module 24209 handles orders and invoices'
