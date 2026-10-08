"""Service module 46746: business logic, no crypto."""


def calculate_total_46746(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46746():
    return 'module 46746 handles orders and invoices'
