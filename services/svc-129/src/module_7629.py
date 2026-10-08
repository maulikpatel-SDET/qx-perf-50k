"""Service module 7629: business logic, no crypto."""


def calculate_total_7629(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7629():
    return 'module 7629 handles orders and invoices'
