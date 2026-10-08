"""Service module 46070: business logic, no crypto."""


def calculate_total_46070(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46070():
    return 'module 46070 handles orders and invoices'
