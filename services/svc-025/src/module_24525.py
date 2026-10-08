"""Service module 24525: business logic, no crypto."""


def calculate_total_24525(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24525():
    return 'module 24525 handles orders and invoices'
