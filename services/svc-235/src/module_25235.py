"""Service module 25235: business logic, no crypto."""


def calculate_total_25235(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25235():
    return 'module 25235 handles orders and invoices'
