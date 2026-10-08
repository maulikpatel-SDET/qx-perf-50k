"""Service module 35127: business logic, no crypto."""


def calculate_total_35127(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35127():
    return 'module 35127 handles orders and invoices'
