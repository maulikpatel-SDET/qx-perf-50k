"""Service module 19235: business logic, no crypto."""


def calculate_total_19235(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19235():
    return 'module 19235 handles orders and invoices'
