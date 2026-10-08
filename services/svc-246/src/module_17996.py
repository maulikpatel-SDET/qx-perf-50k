"""Service module 17996: business logic, no crypto."""


def calculate_total_17996(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17996():
    return 'module 17996 handles orders and invoices'
