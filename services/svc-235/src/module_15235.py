"""Service module 15235: business logic, no crypto."""


def calculate_total_15235(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15235():
    return 'module 15235 handles orders and invoices'
