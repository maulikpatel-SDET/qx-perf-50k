"""Service module 27209: business logic, no crypto."""


def calculate_total_27209(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27209():
    return 'module 27209 handles orders and invoices'
