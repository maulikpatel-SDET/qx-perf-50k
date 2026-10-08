"""Service module 7277: business logic, no crypto."""


def calculate_total_7277(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7277():
    return 'module 7277 handles orders and invoices'
